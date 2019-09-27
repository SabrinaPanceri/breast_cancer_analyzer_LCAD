# python viewer.py Calc-Test_P_00127_RIGHT_CC_MALIGNANT.png input5.txt

import cv2
import sys
import numpy as np
import torch
from torchvision import transforms, models
import torch.nn as nn 
from numpy import float32, dtype



def normalization(imagePath):
           
    Y, X = imagePath.shape
#     acumulador = np.zeros(Y, dtype=float32)
    acumulador = 0.0

    for i in range(0, Y, 1):
        for j in range(0, X, 1):
            print(i,j)
            
            media = np.mean(imagePath[i])
            acumulador += imagePath[i]
            
        print(imagePath[i][j])
        print(media)
        print(acumulador)                
#         print(acumulador[i]/6272)
            
            


def main(args):
    fileName = str(args[1])
    training_dataset_file = open(fileName)
    
    for line in training_dataset_file:
        aux = line.split('\n')
        imageName = aux[0]
        
        imagePath = cv2.imread(imageName, 0)
        imagePath_2 = imagePath/255
        normalization(imagePath_2)
        
    
    training_dataset_file.close()
    

    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv)) 

