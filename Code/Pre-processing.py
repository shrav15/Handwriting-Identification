import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import random
import os
from sklearn import svm

from sklearn.model_selection import train_test_split
"""
TODO:
Add code that removes blank rows/columns from the input image. I will probably then add the same number of rows/columns at the bottom/right side
so that it doesn't break all of the other code. 
"""

    
def extract_samples(img, imsize, spots):
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

    
def print_samples(title, sample_list):
    """
        Prints all of the samples available in an array of samples. 
        Parameters
        ----------
        title : string
            The title for each image. A number will be appended to it. 
        sample_list : list, containing 20 elements. 
            A list of 20 image samples. 
        Returns
        -------
        None.  
    """


    try:
        print_samples.fc += 1
    except AttributeError:
        print_samples.fc = 1
    
    
    rows=4
    columns=5
    i=0
    fig, axs = plt.subplots(num = print_samples.fc, nrows = rows, ncols = columns)
    fig.tight_layout(pad=1)

    print("\n"+title+"\n")
    for i in range(20):
        axs.flat[i].imshow(sample_list[i], cmap = 'Greys_r', vmin = 0, vmax = 255)
        axs.flat[i].set_title(title+" "+str(i+1))
        #print(str(i+1) +"\tMax:"+str(np.amax(sample_list[i])) + "\tMin:"+str(np.amin(sample_list[i])))
        #if(np.amax(sample_list[i]) == np.amin(sample_list[i])):
        #    print("flag")
    
    



def get_samples(sr_no, dict_sample, source):
    """
        Takes a set of random samples from an image, after applying multiple filters.  
        Parameters
        ----------
        sr_no : int
            Serial number for each dictionary element. 
            Represents the group from which the images came from.
        dict_sample : dictionary
            Contains all the data for a particular filter of the images.
        source: string
            Folder inside which the images are stored. 
        Returns
        -------
        None.  
    """
    
    os.chdir(source)
    list_samples = []
    for f in os.listdir():
        img = cv2.imread(f,0)
        file,_ = os.path.splitext(f)
        file_name = file[:3]
        list_samples.append(int(file_name))
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
        # random ranges are = (size of image-safety bound) - size of box (max is 100x100)

        random.seed()
        spotsX = random.sample(range((1300-350)-100), 20)
        spotsY = random.sample(range((980-100)-100), 20)
        spots = [*zip(spotsX,spotsY)]
        # figure number, image, title, sample size, locations

        normal_img   = extract_samples(sample, [100,100], spots)
        lowpass_img  = extract_samples(lowpass, [100,100], spots)
        highpass_img = extract_samples(highpass, [100,100], spots)
        threshed_img = extract_samples(threshed, [100,100], spots)

        # Storing in Dict 
        dict_sample[sr_no][file_name] = {}
        dict_sample[sr_no][file_name]['sample']   = normal_img
        dict_sample[sr_no][file_name]['lowpass']  = lowpass_img
        dict_sample[sr_no][file_name]['highpass'] = highpass_img
        dict_sample[sr_no][file_name]['threshold']= threshed_img
    
    return dict_sample,list_samples




def get_train_test (type_data):

    # As for now only working for P1 normal condtion 
    source = 'D:/documents__/7th sem/fyp/firemaker/300dpi/p1-copy-normal/'
    #source = 'C:/Users/lenovo/Desktop/Educate/FYP/firemaker/300dpi/p1-copy-normal/'
    dict_sample = {}
    sr_no = '01'
    dict_sample[sr_no] = {}
    get_samples(sr_no, dict_sample, source)
    lowpass_data=[]
    y_lowpass=[]
    highpass_data=[]
    y_highpass=[]
    sample_data=[]
    y_sample=[]
    threshold_data=[]
    y_threshold =[]
    for i in dict_sample:
        for j in dict_sample[i]:
            for k in dict_sample[i][j]:
                if k =='lowpass':
                    sum_sample = dict_sample[i][j][k]
                    for x in sum_sample:
                        lowpass_data.append(x.flatten())
                        y_lowpass.append(int(j))



                elif k == 'highpass':
                    sum_sample = dict_sample[i][j][k]
                    for x in sum_sample:
                        highpass_data.append(x.flatten())
                        y_highpass.append(int(j))

                elif k == 'sample':
                    sum_sample = dict_sample[i][j][k]
                    for x in sum_sample:
                        sample_data.append(x.flatten())
                        y_sample.append(int(j))
                else :
                    sum_sample = dict_sample[i][j][k]
                    for x in sum_sample:
                        threshold_data.append(x.flatten())
                        y_threshold.append(int(j))

    if type_data == 'lowpass':
        # Covert list to array 
        Y = np.array(y_lowpass)
        X = np.array(lowpass_data)
    elif type_data == 'highpass':
        # Covert list to array 
        Y = np.array(y_highpass)
        X = np.array(highpass_data)
    elif type_data == 'sample':
        # Covert list to array 
        Y = np.array(y_sample)
        X = np.array(sample_data)
    else :
        # Covert list to array 
        Y = np.array(y_threshold)
        X = np.array(threshold_data)
    return X,Y







def Svm_extraction (X_train,Y_train,X_test,Y_test):


   
    model = svm.SVC(C=1,kernel = 'poly',gamma = 'auto')
    model.fit(X_train,Y_train)
    # Prediction 
    prediction = model.predict(X_test)
 
    # Score 
    acc = model.score(X_test,Y_test)
    print ('accuracy is :',acc)
 








X,Y = get_train_test('lowpass')
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, random_state = 0)
print (X.shape,Y.shape)
Svm_extraction(X_train,Y_train,X_test,Y_test)

"""
print_samples('Lowpass', dict_sample[sr_no]['153']['lowpass'])
print_samples('Highpass', dict_sample[sr_no]['153']['highpass'])
print_samples('Threshold', dict_sample[sr_no]['153']['threshold'])
print_samples('Samples', dict_sample[sr_no]['153']['sample'])
plt.show()
"""
