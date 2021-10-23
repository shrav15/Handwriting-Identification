import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import random

def sampleshower(fc, img, title, imsize, spots):
    """
    Extracts samples from an image and displays them using subplots. 

    Parameters
    ----------
    fc : int
        The figure number.
    img : numpy.ndarray (2D)
        The image from which the samples are taken.
    title : string
        The title of each of the samples. Will be appended by the iterator.
    imsize : numpy.ndarray (1D)
        The size of the samples being taken, in [rows columns] format. 
    spots : tuple
        The locations of the top left corner of each sample. 

    Returns
    -------
    None. 

    """
    imsize = np.array(imsize)
    rows = 4
    columns = 5
    i = 0

    fig, axs = plt.subplots(num = fc, nrows = rows, ncols = columns)
    fig.tight_layout(pad=1)

    for r,c in spots:
        frame = np.zeros([imsize[0]+4,imsize[1]+4])
        frame[2:imsize[0]+2, 2:imsize[1]+2] = img[r:r+imsize[0], c:c+imsize[1]]

        axs.flat[i].imshow(frame, cmap = 'Greys_r')
        axs.flat[i].set_title(title+" "+str(i+1))


        i = i+1
  
    



img = cv2.imread("C:/Users/lenovo/Desktop/FYP/firemaker/300dpi/p1-copy-normal/15201.tif",0)
scale = 40
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
dim = (width, height)
sample = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
sample = sample[325:1300, 100:980]
# basic trimming of top, bot, sides so only main text is visible

lowpass = cv2.GaussianBlur(sample, (5, 5), cv2.BORDER_CONSTANT)
highpass = sample - lowpass
nul, threshed = cv2.threshold(sample, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# the coordinates taken will represent the top left corner of the sampling box
# random ranges are = size of image - size of box (max is 100x100)

random.seed()
spotsX = random.sample(range(975-100), 20)
spotsY = random.sample(range(880-100), 20)
spots = [*zip(spotsX,spotsY)]

# figure number, image, title, sample size, locations
sampleshower(1, sample, "sample", [100,100], spots)
sampleshower(2, lowpass, "lowpass", [100,100], spots)
sampleshower(3, highpass, "highpass", [100,100], spots)
sampleshower(4, threshed, "threshed", [100,100], spots)
plt.show()
