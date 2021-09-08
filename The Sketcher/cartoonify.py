import cv2

# Cartoon has clear edges

img = cv2.imread("Images/hero.jpg")

# 1) Edges

# blurred_img = cv2.medianBlur(img, 5)
# edges = cv2.Canny(blurred_img, 75, 150)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

# 2) Color

color = cv2.bilateralFilter(img, 6, 250, 250)

# 3) Cartoon

cartoon = cv2.bitwise_and(color, color, mask=edges)

# cv2.imshow("Image", img)
# cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edge", edges)
cv2.imshow("color", color)
cv2.imshow("Cartoon", cartoon)
cv2.imwrite("Images/Cartoon.jpg", cartoon)
cv2.waitKey(0)