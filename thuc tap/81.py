import cv2
from matplotlib import pyplot as plt
import numpy as np
from skimage.feature import local_binary_pattern # # pip install scikit-image

KERNEL_WIDTH = 7
KERNEL_HEIGHT = 7
SIGMA_X = 3
SIGMA_Y = 3

def main():
    img = cv2.imread('E:/python/nhandienkhuonmat/thuc tap/3.png', cv2.IMREAD_GRAYSCALE)
    
    # LBP
    out = local_binary_pattern(image=img, P=8, R=1, method='default')
    cv2.imwrite('lbp.jpg', out)
   
    
    # Gaussian blur + LBP
    blur_img = cv2.GaussianBlur(img, ksize=(KERNEL_WIDTH, KERNEL_HEIGHT), sigmaX=SIGMA_X, sigmaY=SIGMA_Y)
    blur_out = local_binary_pattern(image=img, P=8, R=2, method='default')
    cv2.imwrite('E:/python/nhandienkhuonmat/thuc tap/blur.png', blur_img)
    cv2.imwrite('E:/python/nhandienkhuonmat/thuc tap/blur-lbp.png', blur_out)
    plt.imshow(blur_out,cmap ="gray")
    plt.show()
if __name__ == "__main__":
    main()