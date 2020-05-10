import numpy as np
import os
import cv2
import timeit

# number of channels of the dataset image
CHANNEL_NUM = 3

def cal_mean_std(root):
    
    pixel_num = 0 # store all pixel number in the dataset
    channel_sum = np.zeros(CHANNEL_NUM)
    channel_sum_squared = np.zeros(CHANNEL_NUM)

    for idx, d in enumerate(os.listdir(root)):
        path = os.path.join(root,d)

        im = cv2.imread(path) # image in M*N*CHANNEL_NUM shape, channel in BGR order
        im = im/255.0
        pixel_num += (im.size/CHANNEL_NUM)
        channel_sum += np.sum(im, axis=(0, 1))
        channel_sum_squared += np.sum(np.square(im), axis=(0, 1))

    bgr_mean = channel_sum / pixel_num
    bgr_std = np.sqrt(channel_sum_squared / pixel_num - np.square(bgr_mean))
    
    # change the format from bgr to rgb
    rgb_mean = list(bgr_mean)[::-1]
    rgb_std = list(bgr_std)[::-1]
    
    return rgb_mean, rgb_std

# The script assumes that under train_root, there are separate directories for each class
# of training images.
train_root = "D:/Deep Learning/MaskRCNN/bg_fg/"
start = timeit.default_timer()
mean, std = cal_mean_std(train_root)
end = timeit.default_timer()
print("elapsed time: {}".format(end-start))
print("mean:{}\nstd:{}".format(mean, std))
