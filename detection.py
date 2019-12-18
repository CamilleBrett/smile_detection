import cv2

# Locad cascades
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_eye = cv2.CascadeClassifier('haarcascade_eye.xml')
cascade_smile = cv2.CascadeClassifier('haarcascade_smile.xml')

# Define the detection function on face, eyes and smil


def detection(grayscale, img):  # we work on the grayscale pic but also want to show the rvb pic
    # Detect the face : image, scale of the window, min of neighbor zones
    face = cascade_face.detectMultiScale(grayscale, 1.3, 5)
    for (x_face, y_face, w_face, y_face) in face:
        cv2.rectangle(img, (x_face + w_face, y_face+h_face), (255, 130, 0), 2)  # draw the triangles : x,y : upper hand corner; w,h : height and width
    # Interest region
    ri_grayscale = grayscale[y_face:y_face+h_face, x_face:x_face+w_face]
    ri_color = img[y_face:y_face+h_face, x_face:x_face+w_face] 

    # Detect the eyes
    eyes = cascade_eye.detectMultiScale(ri_grayscale, 1.2, 18)
    for (x_eye, y_eye, w_eye, h_eye) in eye:
        cv2.rectangle(ri_color, (x_eye, y_eye), (x_eye+w_eye, y_eye+h_eye), (0, 180, 60), 2)

    # Detect the smile
    smile = cascade_smile.detectMultiScale(ri_grayscale, 1.7, 20)
    for (x_smile, y_smile, w_smile, h_smile) in smile : 
        cv2.rectangle(ri_color, (x_smile, y_smile), (x_smile+w_smile, y_smile+h_smile), (255, 0, 130), 2)

    return img

vc = cv2.VideoCapture(0)

while True:
    _, img = vc.read()
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    final = detection(grayscale, img)
    cv2.imshow('Video', final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vc.release()
cv2.destroyAllWindows()
