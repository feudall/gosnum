from genGosNum import genGosNum
from deform import deformnum
import cv2
import random


tex = list('ABEKMHOPCTYX')
l1 = random.choice(tex)
l2 = random.randint(0, 9)
l3 = random.randint(0, 9)
l4 = random.randint(0, 9)
l5 = random.choice(tex)
l6 = random.choice(tex)
l7 = random.randint(0, 9)
l8 = random.randint(0, 9)
l9 = random.randint(0, 9)
blackout = random.uniform(0.0, 0.9)
scale = random.randint(20, 120)
slant = random.randint(-25, 100)
transform = random.randint(-85, 85)
# print(f'{l1}{l2}{l3}{l4}{l5}{l6}{l7}{l8}{l9}'.upper())

# 'abekmhopctyxd1234567890'
text = f'{l1}{l2}{l3}{l4}{l5}{l6}{l7}{l8}{l9}'
img = genGosNum(text=text, skewX=0, skewY=0, rotate=0, scale=1, blackout=blackout, regcount=False)
img = cv2.imread(f"tmp/{text}.png")
images, cor = deformnum(img, slant=slant, transform=transform, scale=scale)

cv2.imwrite(f'numgos/{text}:slant{slant}:transform{transform}:scale{scale}:blackout{blackout}:{cor}.png', images)

print(text)
print(cor)