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
    raw = rawpy.imread(file_name)
    # np.save(f"{platform.system()}.raw", raw.raw_image)

    raw_cp = raw.raw_image.copy()
    # np.save(f"{platform.system()}.raw_cp", raw_cp)

    linear = linearization(raw_cp)
    # np.save(f"{platform.system()}.linear", linear)

    debayer = demosaic(linear)
    # np.save(f"{platform.system()}.debayer", debayer)
    cv2.imwrite(f"{platform.system()}.debayer.png", debayer)