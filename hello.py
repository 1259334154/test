# import cv2
# import numpy as np
# im = cv2.imread('D:/Desktop/guang.png')
# height, width, channels = im.shape
# new_im = np.ones((height, width, 4)) * 255
# new_im[:, :, :3] = im
# for i in range(height):
#     for j in range(width):
#         if new_im[i, j, :3].tolist() == [255.0, 255.0, 255.0]:
#             new_im[i, j, :] = np.array([255.0, 255.0, 255.0, 0])
# cv2.imwrite('D:/Desktop/tmp_transparent.png', new_im)


import PIL.Image as Image
def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((2,2))
    for h in range(H):
        for l in range(L):
            dot = (l,h)
            color_1 = img.getpixel(dot)
            if color_1 ==color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot,(0,0,0,0))
    return img
img=Image.open('D:/Desktop/guang.png')
img=transparent_back(img)
img.save('D:/Desktop/guang1.png')
