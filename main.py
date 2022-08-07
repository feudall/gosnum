from genGosNum import genGosNum
from deform import deformnum
import cv2
import numpy as np

# 'abekmhopctyxd1234567890'
text = f'h888be175'
img = genGosNum(text=text, skewX=0, skewY=0, rotate=0, scale=1, blackout=0, regcount=False)
img = cv2.imread(f"tmp/{text}.png")
images, cor = deformnum(img, slant=20, transform=50, scale=110)
cv2.imwrite(f'numgos/{text.upper()}:{cor}.png', images)
print(cor)