import cv2

img = cv2.imread('galaxy.jpg', cv2.IMREAD_GRAYSCALE)
print(type(img))
print(img.shape)

cv2.imshow("Galaxy", img)
cv2.waitKey(0)

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('galaxy_resized.jpg', resized_img)