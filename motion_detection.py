from datetime import datetime

import cv2

first_frame = None
status_list = [None, None]
time_list = []

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayscale_frame = cv2.GaussianBlur(grayscale_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = grayscale_frame
        continue

    delta_frame = cv2.absdiff(first_frame, grayscale_frame)
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    # create contours
    (cnts, _) = cv2.findContours(
        threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue

        status = 1

        (x_pos, y_pos, width, height) = cv2.boundingRect(contour)
        cv2.rectangle(
            frame,
            (x_pos, y_pos),
            (x_pos + width, y_pos + height),
            (0, 255, 0),
            3,
        )

    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0:
        time_list.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        time_list.append(datetime.now())

    cv2.imshow("Grayscale Frame", grayscale_frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", threshold_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        if status == 1:
            time_list.append(datetime.now())
        break

print(f"Status list: {status_list}")
print(f"Time list: {time_list}")

video.release()
cv2.destroyAllWindows()
