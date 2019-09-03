import pandas as pd
import numpy as np
import cv2
import os, sys, csv

def crop_cancer(fixPath, path, patientFile, roiFilePath, croppedImagesPath, imageFilePath, cropCancerBool, j):

#    fixPath = "/media/hendrix/18a56f3c-a498-471a-a479-a79073a33aca/CALC/Calc-Training-ROI/CBIS-DDSM/"
#    fixPath = "/media/hendrix/18a56f3c-a498-471a-a479-a79073a33aca/CALC/Calc-Test-ROI/CBIS-DDSM/"
#    path = "/media/hendrix/18a56f3c-a498-471a-a479-a79073a33aca/CALC/Calc-Training-Full/CBIS-DDSM/"
#    path = "/media/hendrix/18a56f3c-a498-471a-a479-a79073a33aca/CALC/Calc-Test-Full/CBIS-DDSM/"

    tempImg = fixPath + roiFilePath[j] 
    image = cv2.imread(tempImg)
    tempImg2 = path + imageFilePath[j]
    examImage = cv2.imread(tempImg2)
    
    smallestBlackPixelAtCoordinateX = 0
    biggestBlackPixelAtCoordinateX = image.shape[1]
    biggestBlackPixelAtCoordinateY = image.shape[0]
    
    
    # LOCALIZA A REGIAO DA ANOMALIA E RETORNA VALORES NECESSARIOS PARA FAZER O CORTE
    
    matrixWithThePositionOfTheWhitePixels = np.where(image == [255]) 
    smallestWhitePixelOfCoordinateX = matrixWithThePositionOfTheWhitePixels[1].min()
    biggestWhitePixelOfCoordinateX = matrixWithThePositionOfTheWhitePixels[1].max()
    smallestWhitePixelOfCoordinateY = matrixWithThePositionOfTheWhitePixels[0].min()
    biggestWhitePixelOfCoordinateY = matrixWithThePositionOfTheWhitePixels[0].max()
    
    distanceBetweenSmallestAndBiggestWhitePixelInCoordinateX = biggestWhitePixelOfCoordinateX - smallestWhitePixelOfCoordinateX
    distanceBetweenSmallestAndBiggestWhitePixelInCoordinateY = biggestWhitePixelOfCoordinateY - smallestWhitePixelOfCoordinateY 
    
    midpointBetweenTheBiggestAndSmallestWhitePixelX = int(distanceBetweenSmallestAndBiggestWhitePixelInCoordinateX/2) + smallestWhitePixelOfCoordinateX
    midpointBetweenTheBiggestAndSmallestWhitePixelY = int(distanceBetweenSmallestAndBiggestWhitePixelInCoordinateY/2) + smallestWhitePixelOfCoordinateY
    
    temporarySmallestWhitePixelOfCoordinateX = midpointBetweenTheBiggestAndSmallestWhitePixelX - 128
    temporarySmallestWhitePixelOfCoordinateY = midpointBetweenTheBiggestAndSmallestWhitePixelY - 128
    temporaryBiggestWhitePixelOfCoordinateX = midpointBetweenTheBiggestAndSmallestWhitePixelX + 128
    temporaryBiggestWhitePixelOfCoordinateY = midpointBetweenTheBiggestAndSmallestWhitePixelY + 128

    #################################################################################

    if cropCancerBool == 0:
        if distanceBetweenSmallestAndBiggestWhitePixelInCoordinateX <= 256 and distanceBetweenSmallestAndBiggestWhitePixelInCoordinateY <= 256:
            if temporaryBiggestWhitePixelOfCoordinateX > biggestBlackPixelAtCoordinateX:
                row = [croppedImagesPath + str(patientFile[j]) + '_NoCancer' + '(' + str(j) + ')' + '.png', '0']
                with open('Calc_Case_Cancer_CC_NC_Cropped_Images.csv', 'a') as csvCrops:
                    writer = csv.writer(csvCrops)
                    writer.writerow(row)
                csvCrops.close()
                cv2.imwrite(os.path.join(croppedImagesPath + str(patientFile[j]) + '_NoCancer' + '(' + str(j) + ')' + '.png'), examImage[(temporarySmallestWhitePixelOfCoordinateY - 512):(temporarySmallestWhitePixelOfCoordinateY - 256), (biggestWhitePixelOfCoordinateX - 256):biggestWhitePixelOfCoordinateX])

            elif temporarySmallestWhitePixelOfCoordinateX < smallestBlackPixelAtCoordinateX:
                row = [croppedImagesPath + str(patientFile[j]) + '_NoCancer' + '(' + str(j) + ')' + '.png', '0'] 
                with open('Calc_Case_Cancer_CC_NC_Cropped_Images.csv', 'a') as csvCrops:
                    writer = csv.writer(csvCrops)
                    writer.writerow(row)
                csvCrops.close()
               
                if biggestWhitePixelOfCoordinateX - 256 < smallestBlackPixelAtCoordinateX: 
                    cv2.imwrite(os.path.join(croppedImagesPath + str(patientFile[j]) + '_NoCancer' + '(' + str(j) + ')' + '.png'), examImage[(temporarySmallestWhitePixelOfCoordinateY - 512):(temporarySmallestWhitePixelOfCoordinateY - 256), 0:256])
                else:    
                    cv2.imwrite(os.path.join(croppedImagesPath + str(patientFile[j]) + '_NoCancer' + '(' + str(j) + ')' + '.png'), examImage[(temporarySmallestWhitePixelOfCoordinateY - 512):(temporarySmallestWhitePixelOfCoordinateY - 256), (biggestWhitePixelOfCoordinateX - 256):biggestWhitePixelOfCoordinateX])
                
            else:
                row = [croppedImagesPath + str(patientFile[j]) + '_NoCancer' + '(' + str(j) + ')' + '.png', '0'] 
                with open('Calc_Case_Cancer_CC_NC_Cropped_Images.csv', 'a') as csvCrops:
                    writer = csv.writer(csvCrops)
                    writer.writerow(row)
                csvCrops.close()
                cv2.imwrite(os.path.join(croppedImagesPath + str(patientFile[j]) + '_NoCancer' + '(' + str(j) + ')' + '.png'), examImage[(temporarySmallestWhitePixelOfCoordinateY - 512):(temporarySmallestWhitePixelOfCoordinateY - 256), (biggestWhitePixelOfCoordinateX - 256):biggestWhitePixelOfCoordinateX])   

    elif cropCancerBool == 1:
        if distanceBetweenSmallestAndBiggestWhitePixelInCoordinateX <= 256 and distanceBetweenSmallestAndBiggestWhitePixelInCoordinateY <= 256:
            if temporaryBiggestWhitePixelOfCoordinateX > biggestBlackPixelAtCoordinateX:
                row = [croppedImagesPath + str(patientFile[j]) + '_WithCancer' + '(' + str(j) + ')' + '.png', '1']
                with open('Calc_Case_Cancer_CC_Cropped_Images.csv', 'a') as csvCrops:    
                    writer = csv.writer(csvCrops)
                    writer.writerow(row)
                csvCrops.close()
                cv2.imwrite(os.path.join(croppedImagesPath + str(patientFile[j]) + '_WithCancer' + '(' + str(j) + ')' + '.png'), examImage[temporarySmallestWhitePixelOfCoordinateY:(temporarySmallestWhitePixelOfCoordinateY + 256), (biggestWhitePixelOfCoordinateX - 256):biggestWhitePixelOfCoordinateX])    
             
            
            elif temporarySmallestWhitePixelOfCoordinateX < smallestBlackPixelAtCoordinateX:
                row = [croppedImagesPath + str(patientFile[j]) + '_WithCancer' + '(' + str(j) + ')' + '.png', '1']
                with open('Calc_Case_Cancer_CC_Cropped_Images.csv', 'a') as csvCrops:
                    writer = csv.writer(csvCrops)
                    writer.writerow(row)
                csvCrops.close()
               
                if biggestWhitePixelOfCoordinateX - 256 < smallestBlackPixelAtCoordinateX: 
                    cv2.imwrite(os.path.join(croppedImagesPath + str(patientFile[j]) + '_WithCancer' + '(' + str(j) + ')' + '.png'), examImage[temporarySmallestWhitePixelOfCoordinateY:(temporarySmallestWhitePixelOfCoordinateY + 256), 0:256])   
                else:    
                    cv2.imwrite(os.path.join(croppedImagesPath + str(patientFile[j]) + '_WithCancer' + '(' + str(j) + ')' + '.png'), examImage[temporarySmallestWhitePixelOfCoordinateY:(temporarySmallestWhitePixelOfCoordinateY + 256), (biggestWhitePixelOfCoordinateX - 256):biggestWhitePixelOfCoordinateX])    
          
            else:
                row = [croppedImagesPath + str(patientFile[j]) + '_WithCancer' + '(' + str(j) + ')' + '.png', '1']
                with open('Calc_Case_Cancer_CC_Cropped_Images.csv', 'a') as csvCrops:    
                    writer = csv.writer(csvCrops)
                    writer.writerow(row)
                csvCrops.close()
                cv2.imwrite(os.path.join(croppedImagesPath + str(patientFile[j]) + '_WithCancer' + '(' + str(j) + ')' + '.png'), examImage[temporarySmallestWhitePixelOfCoordinateY:(temporarySmallestWhitePixelOfCoordinateY + 256), (biggestWhitePixelOfCoordinateX - 256):biggestWhitePixelOfCoordinateX])   
    return j


def main(args):
    fixPath = str(args[1])  # caminho do diretorio que contem os diretorios das imagens segmentadas
    path = str(args[2])     # caminho do diretorio que contem os diretorios das imagens dos exames
    croppedImagesPath = str(args[3])  # caminho do diretorio onde as imagens irao ser salvas
    csvFile = pd.read_csv(args[4])    #arquivo csv com as informaçoes de cada imagem
    cropCancerBool = int(args[5])
    patientFile = csvFile.iloc[:,0].tolist()
    imageFilePath = csvFile.iloc[:,1].tolist()
    roiFilePath = csvFile.iloc[:,2].tolist()
    crop = [crop_cancer(fixPath, path, patientFile, roiFilePath, croppedImagesPath, imageFilePath, cropCancerBool, j) for j in range(len(patientFile))]
     
    return 0
 

if __name__ == '__main__':
    sys.exit(main(sys.argv)) 


# =============================================================================
# Para usar esse algoritmo e necessario ter baixado a base CBIS-DDSM

# COM CANCER
# (1) python cropExams.py /home/sabrina/Datasets/CBIS-DDSM/CALC/Calc-Test-ROI/CBIS-DDSM/ /home/sabrina/Datasets/CBIS-DDSM/CALC/Calc-Test-Full/CBIS-DDSM/ /home/sabrina/GIT/breast_cancer_analyzer_LCAD/dataset/cropImages/withCancer/ /home/sabrina/GIT/breast_cancer_analyzer_LCAD/imagePreProcessing/Calc_Case_Cancer_CC_Test_png.csv 1

# (2) python cropExams.py /home/sabrina/Datasets/CBIS-DDSM/CALC/Calc-Training-ROI/CBIS-DDSM/ /home/sabrina/Datasets/CBIS-DDSM/CALC/Calc-Training-Full/CBIS-DDSM/ /home/sabrina/GIT/breast_cancer_analyzer_LCAD/dataset/cropImages/withCancer/ /home/sabrina/GIT/breast_cancer_analyzer_LCAD/imagePreProcessing/Calc_Case_Cancer_CC_Train_png.csv 1

# SEM CANCER
# (3) python cropExams.py /home/sabrina/Datasets/CBIS-DDSM/CALC/Calc-Training-ROI/CBIS-DDSM/ /home/sabrina/Datasets/CBIS-DDSM/CALC/Calc-Training-Full/CBIS-DDSM/ /home/sabrina/GIT/breast_cancer_analyzer_LCAD/dataset/cropImages/noCancer/ /home/sabrina/GIT/breast_cancer_analyzer_LCAD/imagePreProcessing/Calc_Case_Cancer_CC_NC_Train_png.csv 0
# =============================================================================
