import os
import pydicom
from PIL import Image
from PIL.Image import fromarray
import numpy

if __name__ == '__main__':
    dataset = pydicom.read_file("25155.dcm")
    im = fromarray(dataset.pixel_array)
    im.mode = 'I'
    im.point(lambda i: i * (1. / 16)).convert('L').save('my.jpeg')

    import pydicom
    import pylab

    dFile = pydicom.read_file("25155.dcm")  # path to file
    pylab.imshow(dFile.pixel_array, cmap=pylab.cm.bone)
    pylab.savefig('test.jpg')# pylab readings and conversion
    #pylab.show()  # Dispaly