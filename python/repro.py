import numpy as np
import rawpy
import cv2
import platform

file_name = '../example.orf'

def linearization(img):
    img[img > 65000] = img.min()

    img = ((img - img.min()) * (1/(img.max() - img.min()) * 65535)).astype('uint16')
    return img

def demosaic(img):
    img = cv2.demosaicing(img, cv2.COLOR_BayerGB2BGR) 
    return img

if __name__ == '__main__':
    for i in range(3):
        raw = rawpy.imread(file_name)
        # np.save(f"{platform.system()}_{i}.raw", raw.raw_image)

        raw_cp = raw.raw_image.copy()
        # np.save(f"{platform.system()}_{i}.raw_cp", raw_cp)

        linear = linearization(raw_cp)
        # np.save(f"{platform.system()}_{i}.linear", linear)

        debayer = demosaic(linear)
        # np.save(f"{platform.system()}_{i}.debayer", debayer)
        cv2.imwrite(f"{platform.system()}_{i}.debayer.png", debayer)