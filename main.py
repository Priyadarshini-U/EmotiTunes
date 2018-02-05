import sys
from PIL import Image, ImageFilter
import numpy as np

file = sys.argv[1]

im = Image.open( file )
# im.show()

row,col =  im.size
data = np.zeros((row*col, 5))
pixels = im.load()

for i in range(row):
    for j in range(col):
    	# print pixels[i,j]
    	r,g,b, f =  pixels[i,j]
        data[i*col + j,:] = r,g,b,i,j

print data