import cv2 as cv
import numpy as np
import time
from logic import create_mask, apply_cloak_effect


def main():
    cap = cv.VideoCapture(0)

    print("Зачекайте, захоплення фону...")
    time.sleep(2)
    background = 0
    for i in range(60):
        return_val, background = cap.read()
        if not return_val:
            continue

    lower_boundary = np.array([88, 47, 75])
    upper_boundary = np.array([179, 255, 255])

    print("Програма запущена. Натисніть 'ESC' для виходу.")

    while cap.isOpened():
        return_val, frame = cap.read()
        if not return_val:
            break

        mask = create_mask(frame, lower_boundary, upper_boundary)

        output = apply_cloak_effect(frame, background, mask)

        output = cv.flip(output, 1)
        cv.imshow('Invisible Cloak', output)

        if cv.waitKey(1) == 27:
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()