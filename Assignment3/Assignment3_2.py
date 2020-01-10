import cv2
import os
import numpy as np

def main():
    filename = "tokyoskytree_org"
    current_path = os.getcwd()
    FILE_PATH = os.path.join(current_path, filename + ".jpg")

    img = cv2.imread(FILE_PATH)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    fimg = np.fft.fft2(img_gray)
    fimg = np.fft.fftshift(fimg)

    size = img_gray.shape
    filter_matrix = np.zeros(size)

    length = size[0]
    center = size[0] / 2
    R = 50
    for i in range(0, length):
        for j in range(0, length):
            if (i - center) * (i - center) + (j - center) * (j - center) < R * R:
                filter_matrix[i][j] = 1

    fimg = fimg * filter_matrix
    fimg = np.fft.fftshift(fimg)
    ifimg = np.fft.ifft2(fimg)
    ifimg = ifimg.real

    cv2.imwrite("./tokyoskytree_LPF.jpg", ifimg)


if __name__ == '__main__':
    main()