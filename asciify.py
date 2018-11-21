'''
Turns an image into ascii art
'''
import skimage.io as io
import skimage.transform as itfm
import skimage.filters.edges as ed
import numpy as np
import argparse

chars = ' .,-*+~%oa#'
def map_char(x):
    '''Map color in a range to certain character'''
    nlevels = len(chars)
    levels = np.linspace(0, 1, nlevels)
    for i,k in enumerate(levels):
        if x<=k:
            return chars[i]

def asciifier(im):
    '''Convert image array into array of mapped characters'''
    width, height = im.shape
    # ascii_im = np.zeros((width, height), dtype=np.char)
    ascii_im = np.chararray((width, height))
    for i in range(width):
        for j in range(height):
            ascii_im[i][j] = map_char(im[i][j])
    return ascii_im

def stringify(ascii_im):
    '''Convert the character array into strings'''
    width, height = ascii_im.shape
    ascii_str = ''
    for i in range(width):
        for j in range(height):
            ascii_str += str(ascii_im[i][j])[2:-1]
            if ascii_im[i][j]=='':
                ascii_str += ' '
        ascii_str += '\n'
    return ascii_str

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='turn an image into ascii art')
    parser.add_argument('--image', type=str, help='image to be turned into ascii art' )
    parser.add_argument('--dest', type=str, help='destination text file')
    parser.add_argument('--scale', type=float, help='factor by which image is to be scaled down')
    parser.add_argument('--chars', type=str, help='use your own set of characters')
    parser.add_argument('-p', action='store_true', help='Print ascii art on command line')
    parser.add_argument('-i', action='store_true', help='invert colour')
    parser.add_argument('-e', action='store_true', help='draw edges only')
    parser.add_argument('-b', action='store_true',
           help='make the range of values for which a whitespace is printed larger')
    args = parser.parse_args()
    img = io.imread(args.image, as_gray=True)
    if args.chars:
        chars = args.chars
    if args.i:
        #Invert colors
        img = 1-img
    if args.scale:
        #Scale(down) the images
        img = itfm.rescale(img, args.scale)
    if args.e:
        #Draw the image edges only
        img = ed.sobel(img)
    if args.b:
        #Prepend chars with another white space which
        #effectively doubled the range of value for which whitespace is substituted
        chars = ' '+chars
    im = asciifier(img)
    ascii_str = stringify(im)
    if args.dest:
        #Write the ascii art into a destination file
        with open(args.dest, 'w') as dest:
            dest.write(ascii_str)
    if args.p:
        #Print the ascii art on the console
    	print(ascii_str)

