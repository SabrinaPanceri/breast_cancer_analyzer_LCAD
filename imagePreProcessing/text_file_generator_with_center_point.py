import cv2
import os, sys, csv

def text_file_generator_with_center_point(examsPath, listOfFiles, j):
    if listOfFiles[j][0] != listOfFiles[j-1][0]:
        tempImg = listOfFiles[j][0]
        image = cv2.imread(tempImg)
        pathLabels = "labels/"
        pathNewLabels = "newLabels/"
        tempFileName = os.path.basename(listOfFiles[j][0]) 
        fileName = tempFileName.split(".")
        listOfCoordinates = []
        img = os.path.join(pathLabels + fileName[0] + '.txt')
        if os.path.exists(img):
            with open(pathLabels + fileName[0] + '.txt', newline = '') as textFile:
                fileReader = csv.reader(textFile, delimiter = ' ')
                y = 0
            
                for i in fileReader:
                    listOfCoordinates.append(i)
                    label = listOfCoordinates[y][0]
                    minX = listOfCoordinates[y][1].split(".")
                    maxX = listOfCoordinates[y][3].split(".")
                    minY = listOfCoordinates[y][2].split(".")
                    maxY = listOfCoordinates[y][4].split(".")
                    distanceCenterX = (int(maxX[0]) - int(minX[0]))/2
                    distanceCenterY = (int(maxY[0]) - int(minY[0]))/2
                    centralCoordinateX = int(minX[0]) + int(distanceCenterX)
                    centralCoordinateY = int(minY[0]) + int(distanceCenterY)
                    with open(pathNewLabels + fileName[0] + '.txt', 'a') as newLabel:
                        newLabel.write(label + ' ' + str(centralCoordinateX) + ' ' + str(centralCoordinateY) + '\n')
                    y+=1
        
    return j

def main(args):
    examsPath = str(args[1])  
    listOfFiles = []
    with open(examsPath, newline = '') as textFile:
        fileReader = csv.reader(textFile, delimiter = ' ')
        i = 0
        for i in fileReader:
            listOfFiles.append(i)
    crop = [text_file_generator_with_center_point(examsPath, listOfFiles, j) for j in range(len(listOfFiles))]
    return 0
 

if __name__ == '__main__':
    sys.exit(main(sys.argv)) 
