from __future__ import division, print_function
import random #os, shutil, time, 
import numpy as np
import pandas as pd
import cv2
import sys

import torch
from torch.utils.data import Dataset
from torch.utils.data.dataloader import DataLoader


# import torch.nn as nn
# import torch.optim as optim

# from torchvision import models, transforms


NUM_CLASSES = 2

TRAINING = (
        '/home/sabrina/GIT/breast_cancer_analyzer_LCAD/squeezetnet/cbisddsm_train_2019_09_12.txt',
)

TRAINING_DIR = (
        '/home/sabrina/GIT/breast_cancer_analyzer_LCAD/imagePreProcessing',
)

SHUFFLE = True

BATCH_SIZE, ACCUMULATE = 6272, 1

DATASET_SIZE = 6272

NUM_WORKERS = 4


def calculate_mean(training_dataloader):
    mean = torch.empty(3, dtype=torch.float64)
    for data in training_dataloader:
        data = data.type(torch.float64)
        data = data/255.0
        mean += torch.mean(data, dim=[0, 1, 2])

    return (mean/DATASET_SIZE)


def calculate_std(training_dataloader):
    
    std_dev = torch.empty(3, dtype=torch.float64)
    std_dev + torch.std(data, dim=[0, 1, 2])
    
    
    return std_dev


class DatasetFromCSV(Dataset):
    def __init__(self, csv_files, root_dirs, label=None, shuffle=False, dataset_file=None): 
        data = []
        for csv_file, root_dir in zip(csv_files, root_dirs):
            d = pd.read_csv(csv_file, header=None, names=['images', 'labels'], delim_whitespace=True)
            if label != None:
                d = d.loc[d['labels'] == label].reset_index().drop('index', 1)
            if root_dir != '':
                d['images'] = root_dir + ('' if root_dir.endswith('/') else '/') + d['images']
            data.append(d)
        if len(data) == 1:
            data = data[0]
        else:
            data = pd.concat(data).reset_index().drop('index', 1)
        self.data_len = len(data)

        if shuffle:
            perm = np.arange(self.data_len)
            random.shuffle(perm)
            data = data.iloc[perm].reset_index().drop('index', 1)

        self.images = np.asarray(data.iloc[:, 0])
        self.labels = np.asarray(data.iloc[:, 1])


#         if dataset_file != None:
#             with open(dataset_file, 'w') as dataset:
#                 for image, label in zip(self.images, self.labels):
#                     dataset.write(image + ' ' + str(label) + '\n')

    def __len__(self):
        return self.data_len

    def __getitem__(self, i):
        image = cv2.imread(self.images[i], 3)
        return image


def main(args):
    
    training_dataset_file = str(args[1])
    
    
    with open(training_dataset_file, 'r') as DATASET_FILE:

        training_dataset = DatasetFromCSV(TRAINING, TRAINING_DIR, shuffle=SHUFFLE, dataset_file=DATASET_FILE)
        training_dataloader = DataLoader(training_dataset, BATCH_SIZE, num_workers=NUM_WORKERS)    
        
        mean = calculate_mean(training_dataloader)
        
        print(mean)
#         print(std)
        
    
        
    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv)) 