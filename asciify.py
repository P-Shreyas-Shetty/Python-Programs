'''
Turns an image into ascii art
'''
import skimage.io as io
import skimage.transform as itfm
import numpy as np
import argparse

chars = '.,-*+~%oa#'

def map_char(x, nlevels):
    levels = np.linspace(0, 1, nlevels)
    for i,k in enumerate(levels):
        if x<=k:
            return chars[i]

def asciifier(im):
    width, height = im.shape
    # ascii_im = np.zeros((width, height), dtype=np.char)
    ascii_im = np.chararray((width, height))
    for i in range(width):
        for j in range(height):
            ascii_im[i][j] = map_char(im[i][j], 10)
    return ascii_im

def stringify(ascii_im):
    width, height = ascii_im.shape
    ascii_str = ''
    for i in range(width):
        for j in range(height):
            ascii_str += str(ascii_im[i][j])[2:-1]
        ascii_str += '\n'
    return ascii_str

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Turn an image into ascii art')
    parser.add_argument('--image', type=str, help='image to be turned into ascii art' )
    parser.add_argument('--dest', type=str, help='Destination text file')
    parser.add_argument('--scale', type=float, help='Factor by which image is to be scaled down')
    parser.add_argument('-p', action='store_true', help='Print ascii art on command line')
    parser.add_argument('-i', action='store_true', help='invert colour')

    args = parser.parse_args()
    img = io.imread(args.image, as_gray=True)

    if args.i:
        img = 1-img
    if args.scale:
        img = itfm.rescale(img, args.scale)
    im = asciifier(img)
    ascii_str = stringify(im)
    if args.dest:
        with open(args.dest, 'w') as dest:
            dest.write(ascii_str)
    if args.p:
    	print(ascii_str)

