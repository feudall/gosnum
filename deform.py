import cv2
import numpy as np
# from google.colab.patches import cv2_imshow
def deformnum(img, slant=0, transform=0, scale=100):
    # img = cv2.imread("/content/example.png")
    # slant = -25
    # transform = -50
    # scale = 50
    w = 260 / 100 * scale
    h = 56 / 100 * scale


    def proportions(scale=scale, transform=transform, slant=slant):
        transw = abs(transform) / 100 * scale
        transh = abs(transform) / 100 * scale / 4.7
        slantw = abs(slant) / 100 * scale / 4.7
        slanth = abs(slant) / 100 * scale
        return transw, transh, slantw, slanth


    src = np.float32([(140, 344),  # вержний левый угол
                      (660, 344),  # вержний правый угол
                      (140, 456),  # нижний  левый угол
                      (660, 456)])  # нижний  прав угол

    dst = np.float32([(400, 400),  # вержний левый угол   (660, 344)
                      (400, 400),  # вержний правый угол  (140, 344)
                      (400, 400),  # нижний  левый угол   (660, 456)
                      (400, 400)])  # нижний  прав угол    (660, 456)

    # маштабирование
    dst[0][0], dst[0][1] = dst[0][0] - w, dst[0][1] - h
    dst[1][0], dst[1][1] = dst[1][0] + w, dst[1][1] - h
    dst[2][0], dst[2][1] = dst[2][0] - w, dst[2][1] + h
    dst[3][0], dst[3][1] = dst[3][0] + w, dst[3][1] + h
    # print(dst)

    # деформация в право
    if transform > 0:

        transw, transh, s, s1 = proportions(scale=scale, transform=transform, slant=slant)
        #  готово
        dst[0][0], dst[0][1] = (
            dst[0][0] + transw,  # x1
            dst[0][1] - transh  # y1
        )
        dst[1][0], dst[1][1] = (
            dst[1][0] - transw,  # x2
            dst[1][1] + transh  # y2
        )
        dst[2][0], dst[2][1] = (
            dst[2][0] + transw,  # x3
            dst[2][1] + transh  # y3
        )
        dst[3][0], dst[3][1] = (
            dst[3][0] - transw,  # x4
            dst[3][1] - transh  # y4
        )
        # print('деформация вправо')
        # print(dst)

    # деформация в лево
    elif transform < 0:

        # готово
        transw, transh, s, s1 = proportions(scale=scale, transform=transform, slant=slant)

        dst[0][0], dst[0][1] = (
            dst[0][0] + transw,  # x1
            dst[0][1] + transh  # y1
        )
        dst[1][0], dst[1][1] = (
            dst[1][0] - transw,  # x2
            dst[1][1] - transh  # y2
        )
        dst[2][0], dst[2][1] = (
            dst[2][0] + transw,  # x3
            dst[2][1] - transh  # y3
        )
        dst[3][0], dst[3][1] = (
            dst[3][0] - transw,  # x4
            dst[3][1] + transh  # y4
        )
        # print('деформация влево')
        # print(dst)

    else:
        pass

    # наклон в перед
    if slant > 0:
        if transform > 0:
            t, t1, slantw, slanth = proportions(scale=scale, transform=transform, slant=slant)

            dst[0][0], dst[0][1] = (
                dst[0][0] + slantw * 4.7,
                dst[0][1] + slanth
            )
            dst[1][0], dst[1][1] = (
                dst[1][0] + slantw * 4.7,
                dst[1][1] + slanth
            )
            dst[2][0], dst[2][1] = (
                dst[2][0] - slantw * 4.7,
                dst[2][1] + slanth
            )
            dst[3][0], dst[3][1] = (
                dst[3][0] - slantw * 4.7,
                dst[3][1] + slanth
            )
            # print('наклон в перед и деформация вправо')
            # print(dst)

        if transform < 0:
            t, t1, slantw, slanth = proportions(scale=scale, transform=transform, slant=slant)

            dst[0][0], dst[0][1] = (
                dst[0][0] - slantw * 4.7,
                dst[0][1] + slanth
            )
            dst[1][0], dst[1][1] = (
                dst[1][0] - slantw * 4.7,
                dst[1][1] + slanth
            )
            dst[2][0], dst[2][1] = (
                dst[2][0] + slantw * 4.7,
                dst[2][1] + slanth
            )
            dst[3][0], dst[3][1] = (
                dst[3][0] + slantw * 4.7,
                dst[3][1] + slanth
            )
            # print('наклон в перед и деформация влево')
            # print(dst)

    # наклон в назад
    if slant < 0:
        if transform > 0:
            t, t1, slantw, slanth = proportions(scale=scale, transform=transform, slant=slant)

            dst[0][0], dst[0][1] = (
                dst[0][0] - slantw * 4.7,
                dst[0][1] + slanth
            )
            dst[1][0], dst[1][1] = (
                dst[1][0] - slantw * 4.7,
                dst[1][1] + slanth
            )
            dst[2][0], dst[2][1] = (
                dst[2][0] + slantw * 4.7,
                dst[2][1] + slanth
            )
            dst[3][0], dst[3][1] = (
                dst[3][0] + slantw * 4.7,
                dst[3][1] + slanth
            )
            # print('наклон назад и деформация вправо')
            # print(dst)

        if transform < 0:
            t, t1, slantw, slanth = proportions(scale=scale, transform=transform, slant=slant)

            dst[0][0], dst[0][1] = (
                dst[0][0] + slantw * 4.7,
                dst[0][1] + slanth
            )
            dst[1][0], dst[1][1] = (
                dst[1][0] + slantw * 4.7,
                dst[1][1] + slanth
            )
            dst[2][0], dst[2][1] = (
                dst[2][0] - slantw * 4.7,
                dst[2][1] + slanth
            )
            dst[3][0], dst[3][1] = (
                dst[3][0] - slantw * 4.7,
                dst[3][1] + slanth
            )
            # print('наклон в назад и деформация влево')
            # print(dst)

    h, w = img.shape[:2]
    # use cv2.getPerspectiveTransform() to get M, the transform matrix, and Minv, the inverse
    M = cv2.getPerspectiveTransform(src, dst)
    # use cv2.warpPerspective() to warp your image to a top-down view
    warped = cv2.warpPerspective(img, M, (w, h), flags=cv2.INTER_LINEAR)
    # cv2_imshow(warped)
    # cv2.destroyAllWindows()
    # coordinates = {}
    # for i in range(1, 5):
    #     coordinates[f"x{i} y{i}"] = (dst[i - 1][0], dst[i - 1][1])
    lx = []
    ly = []
    for val in dst:
        lx.append(val[0])
        ly.append(val[1])
    xmax = max(lx)
    xmin = min(lx)
    ymax = max(ly)
    ymin = min(ly)           # [((420 + 98) / 2) / 640, ((462 + 345) / 2) / 480, 322 / 640, 117 / 480] 'равны' [0.4046875, 0.840625, 0.503125, 0.24375].
    cor = [0, ((xmax + xmin) / 2) / 800, ((ymax + ymin) / 2) / 800, (xmax - xmin) / 800, (ymax - ymin) / 800]
    # with open('tmp/annotations')
    #     f.write(index + '\n')



    return warped, cor


if __name__ == '__main__':
    img = cv2.imread('tmp/num/A002MT529.png')
    images, cor = deformnum(img, slant=30, transform=100, scale=100)
    # cv2.imwrite('deform.png', images)
    print(cor)
