import cv2

first_frame = None
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    grayscale_capture = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if first_frame is None:
        first_frame = grayscale_capture

    cv2.imshow("Capturing...", grayscale_capture)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
