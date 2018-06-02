import os
import pydicom
import shutil
from PIL.Image import fromarray


def unZip(filePath, fileName):
    import gzip
    import shutil
    with gzip.open(filePath + "\\" + fileName, 'rb') as f_in:
        with open(filePath + "\\" + str(fileName).replace('.gz', ''), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def walk():
    rootDir = 'D:\shotsNamed'
    newRoot = 'D:\shotsNamed'
    for dirName, subDirList, fileList in os.walk(rootDir):
        for fname in fileList:
            string_fname = str(fname)
            if (str(fname).endswith('.dcm')):
                dataset = pydicom.read_file(os.path.join(dirName, fname))
                new_name = fname.split('.')[0] + '.jpg'
                im = fromarray(dataset.pixel_array)
                im.mode = 'I'
                im.point(lambda i: i * (1. / 16)).convert('L').save(os.path.join(dirName, new_name))
                print('\t%s %s %s' % (fname, dirName, new_name))


if __name__ == '__main__':
    walk()
