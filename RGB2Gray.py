import sys
import cv2
from PIL import Image

def main():
    infile = "./food.jpg"
    outfile = "./food_gray.jpg"

    img_bgr = cv2.imread(infile)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)  # RGB2〜 でなく BGR2〜 を指定
    cv2.imwrite(outfile, img_gray)

if __name__ == '__main__':
    main()