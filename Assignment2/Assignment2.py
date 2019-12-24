import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram_equalization(filename):
    current_path = os.getcwd()
    infile_path = os.path.join(current_path, filename + ".jpg")
    outfile_path_gray = os.path.join(current_path, filename + "_gray" + ".jpg")
    outfile_path = os.path.join(current_path, filename + "_equ" + ".jpg")

    img = cv2.imread(infile_path)

    # make gray img
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(outfile_path_gray, img_gray)

    # get hist
    hist, bins = np.histogram(img_gray.ravel(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    img2 = cdf[img_gray]
    cv2.imwrite(outfile_path, img2)

    # if use opencv
    # equ = cv2.equalizeHist(img)
    # cv2.imwrite(outfile_path, equ)

def med_bil_filter(filename):
    current_path = os.getcwd()
    infile_path = os.path.join(current_path, filename + ".png")
    outfile_path_dst = os.path.join(current_path, filename + "_dst" + ".jpg")
    outfile_path = os.path.join(current_path, filename + "_filter" + ".jpg")

    img = cv2.imread(infile_path)
    # median filter
    dst = cv2.medianBlur(img, 5)
    cv2.imwrite(outfile_path_dst, dst)
    # bilateral filter
    bi = cv2.bilateralFilter(dst, 5, 40, 40)
    bi2 = cv2.bilateralFilter(bi, 5, 40, 40)

    cv2.imwrite(outfile_path, bi2)

def main():
    filename1 = "lowcontrast"
    filename2 = "saltpapernoise"

    histogram_equalization(filename1)
    med_bil_filter(filename2)

if __name__ == '__main__':
    main()