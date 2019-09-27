# python viewer.py Calc-Test_P_00127_RIGHT_CC_MALIGNANT.png input5.txt

import cv2
import sys
import numpy as np
import torch
from torchvision import transforms, models
import torch.nn as nn 



def normalization(imagePath):
           
    Y_Max, X_Max, channels = imagePath.shape
    
    aux_mean = np.zeros(shape = [Y_Max, X_Max, channels], dtype = np.float32)

    
    for i in range(0, Y_Max, 1):
        for j in range(0, X_Max, 1):
            print(imagePath[i][j])
            
    exit()


def main(args):
    fileName = str(args[1])
    training_dataset_file = open(fileName)
    
    for line in training_dataset_file:
        aux = line.split('\n')
        print(aux[0])
        imageName = aux[0]
        print(imageName)
        
        imagePath = cv2.imread(imageName, 3)
        
        print(imagePath.shape)
        
        normalization(imagePath)
    
    
    training_dataset_file.close()
    

    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv)) 

