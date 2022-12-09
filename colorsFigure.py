import matplotlib.pyplot as plt
from skimage.filters import sobel
from skimage.morphology import binary_closing, binary_opening
from skimage.measure import label, regionprops
from skimage import color
import numpy as np


def sides(bbox):
    return bb[2] - bb[0], bb[3] - bb[1]


def count_figs(colors, name):
    colors.sort()
    color_set = {}
    for color in colors:
        if len(color_set) > 0:
            last = list(color_set.keys())[-1]

            if color != last:
                if color > last + 0.02:
                    cur_key = color
                    color_set[cur_key] = 1
                else:
                    color_set[cur_key] += 1
            else:
                color_set[cur_key] += 1

        else:
            cur_key = color
            color_set[cur_key] = 1

    print(f'{name}: {color_set}')


image = plt.imread("C:\\progrpython\\img\\balls-and-rects\\balls_and_rects.png")

binary = image.copy()[:, :, 0]
binary[binary > 0] = 1

image = color.rgb2hsv(image)[:, :, 0]

labeled = label(binary)
print('ALL:', np.max(labeled))



colors_r, colors_c = [], []
for region in regionprops(labeled):
    bb = region.bbox
    val = np.max(image[bb[0]:bb[2], bb[1]:bb[3]])

    a, b = sides(bb)
    if a * b == region.area:
        colors_r.append(val)
    else:
        colors_c.append(val)


count_figs(colors_c, 'circle')
count_figs(colors_r, 'rectangle')



