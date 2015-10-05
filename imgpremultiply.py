# premultiply the alpha of images
# does not check if the images are already premultiplied (there is no good way to do this)
# works in place, so have a backup
#
# python 3-friendly
# tested with Pillow for PIL, precompiled Numpy lib

from PIL import Image
import sys
import glob
import numpy

def premultiply(file_list):
    for path in file_list:
        im = Image.open(path).convert('RGBA')
        a = numpy.fromstring(im.tobytes(), dtype=numpy.uint8)
        alphaLayer = a[3::4] / 255.0
        a[::4]  *= alphaLayer
        a[1::4] *= alphaLayer
        a[2::4] *= alphaLayer

        im = Image.frombytes("RGBA", im.size, a.tostring())
        im.save(path)
        print(path)
    

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("usage: %s <list of files to process>" % sys.argv[0])
        sys.exit(1)

    # check for un-expanded wildcard (windows does this)
    if sys.argv[1].find('*') != -1:
        file_list = glob.glob(sys.argv[1])
    else:
        file_list = sys.argv[1:]

    premultiply(file_list)
    sys.exit(0)
