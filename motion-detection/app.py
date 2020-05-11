from detect import MotionDetector
from motion_graph import MotionGraph


def main():
    detector = MotionDetector()
    graph = MotionGraph()

    detector.start()
    graph.show()


if __name__ == '__main__':
    main()