import cv2
import os

def rote_and_scale(img, angle, scale):
    height = img.shape[0]
    width = img.shape[1]
    center = (int(width / 2), int(height / 2))

    angle = angle
    scale = scale
    trans = cv2.getRotationMatrix2D(center, angle, scale)
    img2 = cv2.warpAffine(img, trans, (width, height))

    return img2

def main():
    filename = "tokyoskytree_org"
    current_path = os.getcwd()

    FILE_PATH = os.path.join(current_path, filename + ".jpg")
    img = cv2.imread(FILE_PATH)

    img_30 = rote_and_scale(img, 30.0, 1.0)
    cv2.imwrite("./tokyoskytree_30.jpg", img_30)

    img_30_flip = cv2.flip(img_30, 1) #flipcode > 0 左右反転
    cv2.imwrite("./tokyoskytree_30_flip.jpg", img_30_flip)

    img_30_flip_10 = rote_and_scale(img_30_flip, 1.0, 10.0)
    cv2.imwrite("./tokyoskytree_30_flip_10.jpg", img_30_flip_10)

if __name__ == '__main__':
    main()