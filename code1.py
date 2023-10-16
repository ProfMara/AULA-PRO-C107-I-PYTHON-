import cv2
video = cv2.VideoCapture("ball.mp4")

while True:

    ret, frame = video.read()

    if ret:
        cv2.imshow("video", frame)
        
    if cv2.waitKey(2)==32:
        break

video.release()
cv2.destroyAllWindows()
