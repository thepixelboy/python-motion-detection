import cv2

first_frame = None
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayscale_frame = cv2.GaussianBlur(grayscale_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = grayscale_frame
        continue

    delta_frame = cv2.absdiff(first_frame, grayscale_frame)
    delta_frame_threshold = cv2.threshold(
        delta_frame, 30, 255, cv2.THRESH_BINARY
    )[1]

    cv2.imshow("Grayscale Frame", grayscale_frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", delta_frame_threshold)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
