import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import random
import os

    
def sampleshower(img, imsize, spots):
        """
        Extracts samples from an image and returns them.  

        Parameters
        ----------
        img : numpy.ndarray (2D)
            The image from which the samples are taken.
        imsize : numpy.ndarray (1D)
            The size of the samples being taken, in [rows columns] format. 
        spots : tuple
            The locations of the top left corner of each sample. 

        Returns
        -------
        samples : list
            A list of image samples.  

        """
        imsize = np.array(imsize)
        samples = []


        for r,c in spots:
            frame = np.zeros([imsize[0],imsize[1]])
            frame[0:imsize[0], 0:imsize[1]] = img[r:r+imsize[0], c:c+imsize[1]]
            samples.append(frame)


        return samples

    
def print_samples(Sample,sample_list):
    fc=1
    rows=4
    columns=5
    i=0
    fig, axs = plt.subplots(num = fc, nrows = rows, ncols = columns)
    fig.tight_layout(pad=1)
    title = Sample

    for i in range(20):

        axs.flat[i].imshow(sample_list[i], cmap = 'Greys_r')
        axs.flat[i].set_title(title+" "+str(i+1))
        print(i)
    plt.show()



def get_samples(sr_no,dict_sample,source):
    
    os.chdir(source)
    for f in os.listdir():
        img = cv2.imread(f,0)
        file,_ = os.path.splitext(f)
        file_name = file[:3]
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
        normal_img = sampleshower( sample, [100,100], spots)
        lowpass_img = sampleshower( lowpass, [100,100], spots)
        highpass_img = sampleshower( highpass, [100,100], spots)
        threshed_img = sampleshower(threshed, [100,100], spots)

        # Storing in Dict 
        dict_sample[sr_no][file_name]={}
        dict_sample[sr_no][file_name]['sample']=normal_img
        dict_sample[sr_no][file_name]['lowpass']=lowpass_img
        dict_sample[sr_no][file_name]['Highpass']=highpass_img
        dict_sample[sr_no][file_name]['Threshold']=threshed_img
    return dict_sample




source = 'D:/documents__/7th sem/fyp/firemaker/300dpi/p1-copy-normal/'
dict_sample = {}
sr_no = '01'
dict_sample[sr_no] = {}
get_samples(sr_no,dict_sample,source)
print_samples('Lowpass',dict_sample[sr_no]['153']['lowpass'])
