# python crop_mmamo.py aux_files/test_dataset.txt


import cv2
import sys
import numpy as np


def image_crop_full_mammo(imageName, imagePath):
           
    Y_Max, X_Max, channels = imagePath.shape

    # print(imageName)
    
    aux_fileName = imageName.split('_set/') 
    # print(aux_fileName)
 
    fileName = aux_fileName[1].split('.')
    
    print(fileName)

    # exit()
        
    scale_percent = 15 # percent of original size
    width = int(imagePath.shape[1] * scale_percent / 100)
    height = int(imagePath.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(imagePath, dim, interpolation = cv2.INTER_AREA)
    
    classificada = imagePath
    classificada_resized = cv2.resize(classificada, dim, interpolation = cv2.INTER_AREA)

    print(fileName[0])

    total_cropy = 0

    for i in range(0, Y_Max, 256):
        for j in range(0, X_Max, 256):
            cropped_img = imagePath[i:i+256, j:j+256]
            
            if ((cropped_img == 0).all() or cropped_img.shape != (256,256,3)):
                break
            else:
                total_cropy += 1
                resized_copy = resized.copy()
                cv2.rectangle(resized_copy, ((int)(j*scale_percent/100), 
                                         (int)(i*scale_percent/100)), ((int)((j+256)*scale_percent/100),
                                                                       (int)((i+256)*scale_percent/100)), (0,0,255), thickness=3)
                
                
                cv2.imwrite(('crop_mammo_test_set/'+fileName[0] +'_'+ 'Crop_'+ str(total_cropy) + '.png'), cropped_img)
                

                window_cropped = 'CROP_'+fileName[0]
                window_classified = 'CLASSIFIED_'+fileName[0]
                
                cv2.namedWindow(window_cropped)
                cv2.moveWindow(window_cropped, 0, 150)
                cv2.imshow(window_cropped, cropped_img)
                
                cv2.namedWindow(window_classified)
                cv2.moveWindow(window_classified, 700, 150)
                cv2.imshow(window_classified, classificada_resized)
                cv2.waitKey(100)

    print('total_cropy = ', total_cropy)
    
    # print("[Correct marker area] = ", (cancer_area) )
    
    cv2.destroyAllWindows() # close displayed windows



def main(args):
    fileName = str(args[1])
    
    
    input_net = open(fileName)
    
    for line in input_net:
        
        str_aux = line.split('\n')
        
        aux = str_aux[0].split(',')
        
        imageName = aux[0]
        

        imagePath = cv2.imread(imageName, 1)
        
        
        
        image_crop_full_mammo(imageName, imagePath)
    
    
    input_net.close()
    

    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv)) 


