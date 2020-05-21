import cv2
import matplotlib.pyplot as plt


def detect_faces(cascade, image, scale_factor=1.1):
    image_copy = image.copy()
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scale_factor, minNeighbors=5)
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 3)

    return image_copy


def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


haar_cascade_face = cv2.CascadeClassifier(
    r'F:\lab_03_02_20\data-mining-langs\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml'
)

test_image1 = cv2.imread('facial-recognition.png')
faces = detect_faces(haar_cascade_face, test_image1)
plt.imshow(convertToRGB(faces))
cv2.imwrite('image-1.png', faces)

test_image1 = cv2.imread('grouping.jpg')
faces = detect_faces(haar_cascade_face, test_image1)
plt.imshow(convertToRGB(faces))
cv2.imwrite('image-2.png', faces)

