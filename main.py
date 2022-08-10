from genGosNum import genGosNum
from deform import deformnum
from skimage.io import imsave
from skimage import exposure, img_as_ubyte
import cv2
import random
from noise import noise



def random_text():
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
    scale = random.randint(15, 100)
    slant = random.randint(-25, 60)
    transform = random.randint(-70, 70)
    if scale < 25 or blackout > 0.7:
        nois = 0.00001
    elif scale < 40 or blackout > 0.6:
        nois = random.uniform(0.0, 0.05)
    else:
        nois = random.uniform(0.0, 0.16)
    regcount = random.choice([True, False])
    if regcount:
        text = (l1, l2, l3, l4, l5, l6, l7, l8)
    else:
        text = (l1, l2, l3, l4, l5, l6, l7, l8, l9)

    text = "".join(map(str, text))
    settings = (blackout, scale, slant, transform, nois, regcount)
    return text, settings

def random_render_num():
    path_num = 'tmp/num'
    path_num_noise = 'tmp/noise_num'
    text, setg = random_text()
    genGosNum(text=text, path=path_num, skewX=0, skewY=0, rotate=0, scale=1, blackout=setg[0], regcount=setg[5])

    img = cv2.imread(f"{path_num}/{text}.png")

    # img = exposure.rescale_intensity(img, out_range=(0, 2 ** 31 - 1))



    images, cor = deformnum(img, slant=setg[2], transform=setg[3], scale=setg[1])
    images = noise(images, val=setg[4])
    images = img_as_ubyte(images)
    imsave(f'{path_num_noise}/{text}:slant={setg[2]}:transform={setg[3]}:scale={setg[1]}:blackout={setg[0]}:cordinates={cor}:noise={setg[4]}.png', images)


    # print(text)

for i in range(6000):
    random_render_num()

