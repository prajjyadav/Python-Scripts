import cv2

# Load the cascade which contains all the factors of Human Face for Detection (Original Source : OPEN CV's GitHub Repository)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# To capture video from the Webcam
cap = cv2.VideoCapture(0)

# In order to detect faces from a video file write  ---------> cap = cv2.VideoCapture('Path of File') in place of cap = cv2.VideoCapture(0) 

while True:
    # Read the frame
    _, img = cap.read()

    # Detect the faces
    faces = face_cascade.detectMultiScale(img)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        if w > 100 and h > 100:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 4)

    # Display
    cv2.imshow('Image', img)

    # Closes the webcam when we press the User press "c" Key. User can change the key as per their choice by updating the Key
    k = cv2.waitKey(1)
    if k == ord('c'):                                   
        break
                
# Release the VideoCapture Object
cap.release()

# Destroys all the running windows
cv2.destroyAllWindows()