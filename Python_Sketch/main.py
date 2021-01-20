import cv2

# vid = cv2.VideoCapture(0)

# while(True):

#     ret, frame = vid.read()

#     cv2.imshow('frame', frame)
    
#     if cv2.waitKey(1) & 0xFF == ord(' '):
#         cv2.imwrite('Captured.png', frame)
#         break

# vid.release()

# cv2.destroyAllWindows()

img = cv2.imread('abc.jpg')

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255 - gray_image

blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

inverted_blurred_image = 255 - blurred_img

pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)

cv2.imshow('Original image',img)
cv2.imshow('New image',pencil_sketch_image)
cv2.waitKey(0)
cv2.imwrite('New image.png',pencil_sketch_image)