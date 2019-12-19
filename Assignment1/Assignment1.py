import sys
import os
import numpy as np
import cv2

def resize(image, scale):
    orgHeight, orgWidth  = image.shape[:2]
    size = (int(orgWidth / scale), int(orgHeight / scale))

    reduced_img = cv2.resize(image, size)

    return reduced_img

def grayscale_formula(filename):
    current_path = os.getcwd()
    infile_path = os.path.join(current_path, filename + ".jpg")
    outfile_path = os.path.join(current_path, "image", filename + "_gray" + "_formula.jpg")

    img_bgr = cv2.imread(infile_path)

    img_bgr = resize(img_bgr, 4)

    b, g, r = cv2.split(img_bgr)
    img_gray = np.array(0.3 * r + 0.6 * g + 0.1 * b, dtype='uint8')
    cv2.imwrite(outfile_path, img_gray)

def grayscale_opencv(filename):
    current_path = os.getcwd()
    infile_path = os.path.join(current_path, filename + ".jpg")
    outfile_path = os.path.join(current_path, "image", filename + "_gray" + "_opencv.jpg")

    img_bgr = cv2.imread(infile_path)

    img_bgr = resize(img_bgr, 4)

    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(outfile_path, img_gray)

def bit_plane(filename, bit):
    current_path = os.getcwd()
    infile_path = os.path.join(current_path, "image", filename + "_gray_opencv.jpg")
    outfile_path = os.path.join(current_path, "image", filename + "_gray_bit_plane_" + str(bit) + ".jpg")

    img_bgr = cv2.imread(infile_path)
    b, g, r = cv2.split(img_bgr)

    bit_img = np.where(img_bgr & bit, 255, 0)
    cv2.imwrite(outfile_path, bit_img)


def main():
    filename1 = "food"
    filename2 = "Kitakyushu"

    # use opencv function
    grayscale_opencv(filename1)
    grayscale_opencv(filename2)

    # use 0.3 * r + 0.6 * g + 0.1 * r
    grayscale_formula(filename1)
    grayscale_formula(filename2)

    bit = 1
    for i in range(8):
        bit_plane(filename1, bit)
        bit_plane(filename2, bit)
        bit = bit << 1

if __name__ == '__main__':
    main()