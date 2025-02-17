import cv2

video = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(r"C:\Users\prade\Downloads\haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier(r"C:\Users\prade\Downloads\haarcascade_smile.xml")

# Check if the files loaded correctly
if faceCascade.empty():
    print("Error loading face cascade file!")
if smileCascade.empty():
    print("Error loading smile cascade file!")

while True:
    success, img = video.read()
    if not success:
        break

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImg, 1.1, 4)

    cnt = 500
    keyPressed = cv2.waitKey(1)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 3)
        smiles = smileCascade.detectMultiScale(grayImg, 1.8, 15)

        for sx, sy, sw, sh in smiles:
            img = cv2.rectangle(img, (sx, sy), (sx+sw, sy+sh), (100, 100, 100), 5)
            print("Image " + str(cnt) + " Saved")
            path = r'C:/Users/prade/Downloads/' + str(cnt) + '.jpg'
            cv2.imwrite(path, img)
            cnt += 1
            if cnt >= 503:
                break

    cv2.imshow('live video', img)

    if keyPressed & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
