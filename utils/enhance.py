import cv2
import numpy as np

def img_weighted(img):
    img = cv2.addWeighted(img, 1.5, img, -0.5, 0)

    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    img = cv2.filter2D(img, -1, kernel)

    hue = img[:, :, 0]
    saturation = img[:, :, 1]
    value = img[:, :, 2]
    value = np.clip(value * 1.25, 0, 255)

    img[:, :, 2] = value

    return img
