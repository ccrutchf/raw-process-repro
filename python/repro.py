import numpy as np
import rawpy
import cv2
import platform
import os
from pathlib import Path


file_name = 'P5050051.ORF'
data_path = Path("test_set")

def linearization(img):
    img[img > 65000] = img.min()

    img = ((img - img.min()) * (1/(img.max() - img.min()) * 65535)).astype('uint16')
    return img

def demosaic(img):
    img = cv2.demosaicing(img, cv2.COLOR_BayerGB2BGR) 

    print(img.dtype)

    return img

if __name__ == '__main__':
    for file in os.listdir(data_path.as_posix()):
        print(file)
        filepath = data_path.joinpath(file)

        raw = rawpy.imread(filepath.as_posix())
        # np.save(f"{platform.system()}.raw", raw.raw_image)

        raw_cp = raw.raw_image.copy()
        # np.save(f"{platform.system()}.raw_cp", raw_cp)
        for i in range(100):
            print(raw_cp[0][i])

        linear = linearization(raw_cp)
        # np.save(f"{platform.system()}.linear", linear)

        debayer = demosaic(linear)
        # np.save(f"{platform.system()}.debayer", debayer)
        cv2.imwrite(f"{platform.system()}.{file}.debayer.png", debayer)