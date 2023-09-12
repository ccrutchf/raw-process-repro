import numpy as np
import rawpy
import cv2
import platform
import gc

file_name = '../example.orf'

def linearization(img):
    img[img > 65000] = img.min()

    img2 = ((img - img.min()) * (1/(img.max() - img.min()) * 65535)).astype(np.uint16)
    return img2

def demosaic(img):
    img2 = cv2.demosaicing(img, cv2.COLOR_BayerGB2BGR) 
    return img2

def main():
    raw_list = []

    for i in range(3):
        # with rawpy.imread(file_name) as elephant:
        elephant = rawpy.imread(file_name)
        # raw_list += [elephant]

        linear = linearization(elephant.raw_image)
        debayer = demosaic(linear)
        
        cv2.imwrite(f"{platform.system()}_{i}.debayer.png", debayer)

        elephant.close()

            
if __name__ == '__main__':
    # gc.disable()
    main()
    # gc.enable()
