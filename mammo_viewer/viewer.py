# python viewer.py Calc-Test_P_00127_RIGHT_CC_MALIGNANT.png input5.txt

import cv2
import sys
# import numpy as np
# from numpy import dtype



def image_tester(imageName, imagePath, file_net):
           
    Y_Max, X_Max = imagePath.shape
    
    fileName = imageName.split('.')
        
    scale_percent = 15 # percent of original size
    width = int(imagePath.shape[1] * scale_percent / 100)
    height = int(imagePath.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(imagePath, dim, interpolation = cv2.INTER_AREA)

    
    for i in range(0, Y_Max, 256):
        for j in range(0, X_Max, 256):
            cropped_img = imagePath[i:i+256, j:j+256]

            if ((cropped_img == 0).all() or cropped_img.shape != (256,256)):
                break
            else:
                resized_copy = resized.copy()
                cv2.rectangle(resized_copy, ((int)(j*scale_percent/100), 
                                         (int)(i*scale_percent/100)), ((int)((j+256)*scale_percent/100),
                                                                       (int)((i+256)*scale_percent/100)), (255,0,0), 2)
            
                cv2.imwrite(('cropped/'+fileName[0] +'_'+ str(i)+'_'+ str(j) + '.png'), cropped_img)
                
                with open(file_net, "a") as input_net:
                    input_net.write('cropped/'+fileName[0] +'_'+ str(i)+'_'+ str(j) + '.png\n')
                
                cv2.namedWindow('resized_copy', cv2.WINDOW_AUTOSIZE)
                cv2.imshow('resized_copy', resized_copy)
                cv2.imshow('cropped_img', cropped_img)
                cv2.waitKey(100)
                
        
        
    cv2.destroyAllWindows() # close displayed windows
        


def out_network(file_net, probability_txt):
    
    
#     chamar o scrip de execução da rede aqui
#     passar para o script a imagem crooped
#     pegar o script o valor da probalidade
#     [probabilidade de não ser cancer][probabilidade de SER cancer]
#     criar a nova imagem de acordo com o maior valor
#     a nova imagem sera branca (255), se o maior valor for  [probabilidade de SER cancer]
#     a nova imagem sera preta (0), se o maior valor for  [probabilidade de NÃO SER cancer]


    
    input_net = open(file_net)
    for line in input_net:
        print(line)
    input_net.close()



def main(args):
    imageName = str(args[1])
    imagePath = cv2.imread(imageName, 0)
    file_net = str(args[2])
     
    
#     probability_txt = str(args[3])
    
    image_tester(imageName, imagePath, file_net)
    
#     with open(input_file, "r") as path_image_analised:
#         out_network(path_image_analised)
    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv)) 


