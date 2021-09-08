import cv2

a = input("Enter c for camera shot else p for the stored picture ")

image = 'Images/hero.jpg'

if a=='c':
    vid = cv2.VideoCapture(0)

    while(True):

        ret, frame = vid.read()

        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.imwrite('Images/Captured.png', frame)
            break

    vid.release()

    cv2.destroyAllWindows()

    image = 'Captured.png'

img = cv2.imread(image)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255 - gray_image

blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

inverted_blurred_image = 255 - blurred_img

pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)

cv2.imshow('Original image',img)

cv2.imshow('New image',pencil_sketch_image)

cv2.waitKey(0)

cv2.imwrite('Images/New image.jpg',pencil_sketch_image)