import skimage
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import cv2
from skimage.util import random_noise


image_gray = imread('/content/example.png', as_gray=False)
img_noise = skimage.util.random_noise(image_gray,  mode='gaussian')
img_noise = skimage.util.random_noise(img_noise,  mode='localvar')
img_noise = skimage.util.random_noise(img_noise,  mode='poisson')
img_noise = skimage.util.random_noise(img_noise,  mode='salt')
img_noise = skimage.util.random_noise(img_noise,  mode='pepper')
img_noise = skimage.util.random_noise(img_noise,  mode='s&p')
img_noise = skimage.util.random_noise(img_noise,  mode='speckle')
cv2.imwrite('noise.png', img_noise)
# img_noise = np.clip(image_gray, 0, 1.0)
plt.figure(figsize=(20, 20))
imshow(img_noise)
# cv2.imwrite('noise.png', img_noise)