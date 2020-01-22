import cv2, argparse
import os, sys, csv


def generate_dataset_with_new_names(root, pathList, subList, labelList):
    j = 0
    if j == 0:
        path = pathList[j].split('_')
        pathName = path[0]
        if pathName == 'Calc-Test':
            ImagesPath = root + 'CBIS-DDSM/CALC/Calc-Test-Full/CBIS-DDSM'
            if os.path.isdir(root + 'CBIS-DDSM/new-dataset/' + 'Calc-Test') == False:
                os.mkdir(root + 'CBIS-DDSM/new-dataset/' + 'Calc-Test')
                f = open(root + 'CBIS-DDSM/new-dataset/Calc-Test/' + 'Calc-Test.txt', 'w')
                f.close()

        elif pathName == 'Calc-Training':
            ImagesPath = root + 'CBIS-DDSM/CALC/Calc-Training-Full/CBIS-DDSM'
            if os.path.isdir(root + 'CBIS-DDSM/new-dataset/' + 'Calc-Training') == False:
                os.mkdir(root + 'CBIS-DDSM/new-dataset/' + 'Calc-Training')
                f = open(root + 'CBIS-DDSM/new-dataset/Calc-Training/' + 'Calc-Training.txt', 'w')
                f.close()
                
        elif pathName == 'Mass-Test':
            ImagesPath = root + 'CBIS-DDSM/MASS/Mass-Test-Full/CBIS-DDSM'
            if os.path.isdir(root + 'CBIS-DDSM/new-dataset/' + 'new-dataset/Mass-Test') == False:
                os.mkdir(root + 'CBIS-DDSM/new-dataset/' + 'new-dataset/Mass-Test')
                f = open(root + 'CBIS-DDSM/new-dataset/Mass-Test/' + 'Mass-Test.txt', 'w')
                f.close()
                        
        elif pathName == 'Mass-Training':
            ImagesPath = root + 'CBIS-DDSM/MASS/Mass-Training-Full/CBIS-DDSM'
            if os.path.isdir(root + 'CBIS-DDSM/new-dataset/' + 'Mass-Training') == False:
                os.mkdir(root + 'CBIS-DDSM/new-dataset/' + 'Mass-Training')
                f = open(root + 'CBIS-DDSM/new-dataset/Mass-Training/' + 'Mass-Training.txt', 'w')
                f.close()  

    while j < len(pathList):
        tempImg = ImagesPath + '/' + pathList[j]
        examImage = cv2.imread(tempImg) 
        aux = pathList[j].split('/')
        fileName = aux[0]
        biRADS = labelList[j]
        difficulty = subList[j]
        biggestPixelAtCoordinateX = examImage.shape[1]            
        biggestPixelAtCoordinateY = examImage.shape[0]  
        renamedImagesPath = root + 'CBIS-DDSM/new-dataset/' + pathName + '/'
        
        cv2.imwrite(os.path.join(renamedImagesPath + str(fileName) + '_' + 'BIRADS-' + str(biRADS) + '_' + 'sub-' + str(difficulty) + '.png'), examImage[0:biggestPixelAtCoordinateY,0:biggestPixelAtCoordinateX]) 
        

        with open(renamedImagesPath + str(pathName) + '.txt', 'a+') as myfile:
            myfile.write(renamedImagesPath + '_' + str(fileName) + '_' + 'BIRADS-' +  str(biRADS) + '_' + 'sub-' + str(difficulty) + '.png\n')
        j+=1
    return j


#Passar os parâmetros: o caminho até o dataset CBIS-DDSM dentro da máquina e o nome do arquivo .txt a ser lido  


def main(args):

    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=str, help="the path of CBIS-DDSM")
    parser.add_argument("f", type=str, help="the path of txt file")
    args = parser.parse_args()
    print(args.p)
    print(args.f)
    root = args.p
    if os.path.isdir(root + 'CBIS-DDSM/' + 'new-dataset') == False:
        os.mkdir(root + 'CBIS-DDSM/' + 'new-dataset')
    with open(args.f) as f:
        data = f.readlines()
    reader = csv.reader(data, delimiter=',')
    pathList = []
    labelList = []
    subList = []
    for row in reader:
        pathList.append((row[11]))
        labelList.append((row[8]))
        subList.append((row[10]))


    generate_dataset_with_new_names(root, pathList, subList, labelList)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv)) 