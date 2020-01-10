import os
import cv2
import numpy as np

def main():
    filename = "tokyoskytree_org"
    current_path = os.getcwd()
    FILE_PATH = os.path.join(current_path, filename + ".jpg")

    img = cv2.imread(FILE_PATH)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

if __name__ == '__main__':
    main()