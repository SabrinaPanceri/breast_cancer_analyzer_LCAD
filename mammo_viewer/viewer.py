# python viewer.py Calc-Test_P_00127_RIGHT_CC_MALIGNANT.png input5.txt

import cv2
import sys
import numpy as np
import torch
from torchvision import transforms, models
import torch.nn as nn 



def image_tester(imageName, image_GT, imagePath, net):
           
    Y_Max, X_Max, channels = imagePath.shape
    
    aux_fileName = imageName.split('/') 
 
    fileName = aux_fileName[1].split('.')
        
    scale_percent = 15 # percent of original size
    width = int(imagePath.shape[1] * scale_percent / 100)
    height = int(imagePath.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(imagePath, dim, interpolation = cv2.INTER_AREA)
    
    resized_GT = cv2.resize(image_GT, dim, interpolation = cv2.INTER_AREA)
    
#     classificada = np.zeros(shape = [Y_Max, X_Max, channels], dtype = np.uint8)
    classificada = imagePath
    classificada_resized = cv2.resize(classificada, dim, interpolation = cv2.INTER_AREA)

    print(fileName[0])
    
    for i in range(0, Y_Max, 256):
        for j in range(0, X_Max, 256):
            cropped_img = imagePath[i:i+256, j:j+256]
            cropped_tensor = cropped_img.copy()
            
            if ((cropped_img == 0).all() or cropped_img.shape != (256,256,3)):
                break
            else:
                resized_copy = resized.copy()
                cv2.rectangle(resized_copy, ((int)(j*scale_percent/100), 
                                         (int)(i*scale_percent/100)), ((int)((j+256)*scale_percent/100),
                                                                       (int)((i+256)*scale_percent/100)), (255,0,0), 2)
#                 cv2.imwrite(('cropped/'+fileName[0] +'_'+ str(i)+'_'+ str(j) + '.png'), cropped_img)
                
#                 with open(file_net, "a") as input_net:
#                     input_net.write('cropped/'+fileName[0] +'_'+ str(i)+'_'+ str(j) + '.png\n')

                
                input_class = network_classifier(cropped_tensor, net, fileName[0])
                
#                 print(input_class[0][1])
                
                
                if input_class[0][1] > 0.93:
#                     print('input_class = 0')                    
                    cv2.rectangle(classificada_resized, ((int)(j*scale_percent/100), 
                                         (int)(i*scale_percent/100)), ((int)((j+256)*scale_percent/100),
                                                                       (int)((i+256)*scale_percent/100)), (0,0,255), thickness=-1)
                    
                    cv2.imwrite(('classified/'+ fileName[0] + '.png'), classificada_resized)

                    
                else:
#                     print('input_class = 1')
                    cv2.rectangle(classificada_resized, ((int)(j*scale_percent/100), 
                                         (int)(i*scale_percent/100)), ((int)((j+256)*scale_percent/100),
                                                                       (int)((i+256)*scale_percent/100)), (0,255,0), thickness=-1)

                    cv2.imwrite(('classified/'+ fileName[0] + '.png'), classificada_resized)
                    

#                 cv2.namedWindow('FULL_MAMMO', cv2.WINDOW_AUTOSIZE)
                cv2.imshow('FULL_MAMMO', resized_copy)
                cv2.imshow('cropped_img', cropped_img)
                cv2.imshow('GT_MAMMO', resized_GT)
                cv2.imshow('classificada', classificada_resized)
                
                
                cv2.waitKey(200)
    
    cv2.destroyAllWindows() # close displayed windows
        

def network_classifier(cropped_tensor, net, fileName):
    cropped_tensor = np.transpose(cropped_tensor, [2, 0, 1])[[2, 1, 0]]
    cropped_tensor = cropped_tensor/255
    cropped_tensor = torch.from_numpy(cropped_tensor.astype(np.float32))
    normalize = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])            
    cropped_tensor = normalize(cropped_tensor)
    cropped_tensor_list = np.array([cropped_tensor.tolist()])
    cropped_tensor = torch.from_numpy(cropped_tensor_list.astype(np.float32))
    with torch.no_grad():
        classification = net(cropped_tensor.to('cuda:0'))
        m = nn.Softmax(dim=1)
        batch_s = m(classification)
        batch_s = batch_s.tolist()
#         print(batch_s)
    
        for s in batch_s:
            with open('probabilities/'+ fileName +'.txt', 'a') as ptest:
                ptest.write(str(s[0]) + '\t' + str(s[1]) + '\n')
        
        input_class = batch_s
        
    return input_class
     
def load_matching_name_and_shape_layers(net, new_model_name, new_state_dict):
    print('\n' + new_model_name + ':')
    state_dict = net.state_dict()
    for key in state_dict:
        if key in new_state_dict and new_state_dict[key].shape == state_dict[key].shape:
            state_dict[key] = new_state_dict[key]
            print('\t' + key + ' loaded.')
    net.load_state_dict(state_dict)


def Net():
    model = getattr(models, 'squeezenet1_1')
    net = model(num_classes=2)
    load_matching_name_and_shape_layers(net, 'Torchvision pretrained model', model(pretrained=True).state_dict())
    return net



def main(args):
    fileName = str(args[1])
    INITIAL_MODEL = '/home/sabrina/GIT/breast_cancer_analyzer_LCAD/squeezetnet/runs/squeezenet1_1_60_8.pth'
    torch.multiprocessing.set_start_method('spawn', force=True)
    net = Net().to('cuda:0')
    load_matching_name_and_shape_layers(net, INITIAL_MODEL, torch.load(INITIAL_MODEL))
    
    input_net = open(fileName)
    
    for line in input_net:
        aux = line.split(',')
        imageName = aux[0]
        aux_imageGT = aux[1].split('\n')
        imageGT = aux_imageGT[0]

        imagePath = cv2.imread(imageName, 3)
        image_GT = cv2.imread(imageGT, 3)
        
        image_tester(imageName, image_GT, imagePath, net)
    
    
    input_net.close()
    

    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv)) 


