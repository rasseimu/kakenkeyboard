import cv2
import numpy as np

if __name__ == "__main__":
    # define parameter
    HSV_MIN = np.array([0, 30, 60])
    HSV_MAX = np.array([20, 150, 255])

    # read input image
    img = cv2.imread("./imagefile/pianoCE1.jpg")

    #convert hsv
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #mask hsv region
    mask_hsv = cv2.inRange(img_hsv, HSV_MIN, HSV_MAX)

    # save image
    cv2.imwrite("./imagefile/mask_pianoCE1.jpg", mask_hsv)
