##HEY THERE BUD
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import random
import os
import glob
from tqdm.notebook import tqdm

import albumentations as A

from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_data = glob.glob('../PneumoniaDetectionAI/chest_xray/train/**/*.jpeg')
test_data = glob.glob('../PneumoniaDetectionAI/chest_xray/test/**/*.jpeg')
val_data = glob.glob('../PneumoniaDetectionAI/chest_xray/val/**/*.jpeg')

"""
print(f"Training Set has: {len(train_data)} images")
print(f"Testing Set has: {len(test_data)} images")
print(f"Validation Set has: {len(val_data)} images")
"""
def plot_multiple_img(img_matrix_list, title_list, ncols, main_title=""):
    fig, myaxes = plt.subplots(figsize=(20, 15), nrows=3, ncols=ncols, squeeze=False)
    fig.suptitle(main_title, fontsize = 30)
    fig.subplots_adjust(wspace=0.3)
    fig.subplots_adjust(hspace=0.3)
    for <a onclick="parent.postMessage({'referent':'.kaggle.usercode.11298373.41303076.plot_multiple_img..i'}, '*')">i, (img, title) in enumerate(zip(img_matrix_list, title_list)):
    myaxes[i // ncols][i % ncols].imshow(img)
    myaxes[i // ncols][i % ncols].set_title(title, fontsize=15)
    plt.show()


