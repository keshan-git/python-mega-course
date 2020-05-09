import cv2
import numpy as np
import pandas as pd
from datetime import datetime
from skimage.measure import compare_ssim


def __resize_image_ratio__(image, ratio):
    return cv2.resize(image, (int(image.shape[1] / ratio), int(image.shape[0] / ratio)))


class MotionDetector:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.background_frame = None

        self.detected = False
        self.time_stamp = datetime.now()
        self.result_df = pd.DataFrame(columns=['Start', 'End'])

    def __del__(self):
        cv2.destroyAllWindows()
        self.video_capture.release()

    def __on_motion_detect__(self):
        if self.detected:
            print('Object removed from the view port')
            record = {'Start': self.time_stamp, 'End': datetime.now()}
            print('New record added - {}'.format(record))
            self.result_df = self.result_df.append(record, ignore_index=True )
        else:
            print('New object entered to the view port')
            self.time_stamp = datetime.now()

    def start(self):
        print('Waiting for Background Frame... Press [Y] when ready')
        while True:
            check, frame = self.video_capture.read()

            if self.background_frame is None:
                cv2.imshow("Waiting for Background Frame... [Y] when ready", frame)
                key = cv2.waitKey(1)
                if key == ord('y'):
                    self.background_frame = frame
                    background_frame_gray = cv2.cvtColor(self.background_frame, cv2.COLOR_BGR2GRAY)
                    background_frame_gray = cv2.blur(background_frame_gray, (5, 5))
                    cv2.destroyAllWindows()

                    print('Background frame captured, motion detection running...')
                continue

            current_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            current_frame_gray = cv2.blur(current_frame_gray, (5, 5))

            score, diff = compare_ssim(background_frame_gray, current_frame_gray, full=True)
            diff = (diff * 255).astype('uint8')
            diff_smooth = cv2.blur(diff, (20, 20))
            threshold = cv2.threshold(diff_smooth, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

            contours_frame = frame.copy()
            detected_frame = frame.copy()
            frame.copy()

            current_detected = score < 0.89
            if current_detected != self.detected:
                self.__on_motion_detect__()
                self.detected = current_detected

            if self.detected:
                contours, hierarchy = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cv2.drawContours(contours_frame, contours, -1, (0, 255, 0), 1)

                main_contour = max(contours, key=cv2.contourArea)
                x, y, width, height = cv2.boundingRect(main_contour)
                cv2.rectangle(detected_frame, (x, y), (x + width, y + height), (0, 0, 255), 2)

            preview = np.hstack((__resize_image_ratio__(self.background_frame, 2),
                                 __resize_image_ratio__(contours_frame, 2),
                                 __resize_image_ratio__(detected_frame, 2)))

            process_preview = np.hstack((__resize_image_ratio__(diff, 2),
                                         __resize_image_ratio__(diff_smooth, 2),
                                         __resize_image_ratio__(threshold, 2)))

            cv2.imshow("Motion Detection", process_preview)
            cv2.imshow("Motion Detection - Result", preview)

            key = cv2.waitKey(1)
            if key == ord('q'):
                if self.detected:
                    self.__on_motion_detect__()
                break

        print('Writing detection times in to CSV file')
        self.result_df.to_csv('detection.csv')
