import os
import cv2
import math
import numpy as np

def main():
    filename = "tokyoskytree_org"
    current_path = os.getcwd()
    FILE_PATH = os.path.join(current_path, filename + ".jpg")

    img = cv2.imread(FILE_PATH)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    fimg = np.fft.fft2(img_gray)
    # fimg = np.fft.fftshift(fimg)
    # ifimg = np.fft.ifft2(fimg)
    # cv2.imwrite("./tokyoskytree_FFT.jpg", ifimg.real)

    # make
    size = img_gray.shape
    filter_matrix = np.zeros(size)
    h, w = img_gray.shape
    center = np.array([(h-1)/2, (w-1)/2])
    R = 1
    for i in range(0, w):
        for j in range(0, h):
            if (i - center[1]) * (i - center[1]) + (j - center[0]) * (j - center[0]) < R * R:
                filter_matrix[j][i] = 1/(2*math.pi*R**2)

    filter_matrix = np.fft.fftshift(filter_matrix)
    filter_matrix = np.fft.fft2(filter_matrix)

    fout = np.zeros(size, dtype=np.complex)
    fout = fimg * filter_matrix
    ifout = np.fft.ifft2(fout)
    ifout = ifout.real

    cv2.imwrite("./tokyoskytree_PSF.jpg", ifout)



if __name__ == '__main__':
    main()