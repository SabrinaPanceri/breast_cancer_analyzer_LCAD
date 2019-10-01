import cv2
import sys


def rotate_image(imagePath):
    # read image as grey scale
    img = cv2.imread(imagePath)
    # get image height, width
    (h, w) = img.shape[:2]
    # calculate the center of the image
    center = (w / 2, h / 2)
    
    aux_fileName = imagePath.split('/') 
 
    fileName = aux_fileName[1].split('.')
        
     
    angle90 = 90
    angle180 = 180
    angle270 = 270
     
    scale = 1.0
     
    # Perform the counter clockwise rotation holding at the center
    # 90 degrees
    M = cv2.getRotationMatrix2D(center, angle90, scale)
    rotated90 = cv2.warpAffine(img, M, (h, w))
     
    # 180 degrees
    M = cv2.getRotationMatrix2D(center, angle180, scale)
    rotated180 = cv2.warpAffine(img, M, (w, h))
     
    # 270 degrees
    M = cv2.getRotationMatrix2D(center, angle270, scale)
    rotated270 = cv2.warpAffine(img, M, (h, w))
     
    
    window_original = 'ORIGINAL_'+fileName[0]
    window_90 = 'ROTATED_90_'+fileName[0]
    window_180 = 'ROTATED_180_'+fileName[0]
    window_270 = 'ROTATED_270_'+fileName[0]
    
    
    cv2.namedWindow(window_original)
    cv2.moveWindow(window_original, 0, 0)
#     cv2.imshow(window_original,img)
#     cv2.waitKey(10) # waits until a key is pressed
    # cv2.destroyAllWindows() # destroys the window showing image
    
    cv2.namedWindow(window_90)
    cv2.moveWindow(window_90, 0, 370)
#     cv2.imshow(window_90,rotated90)
    cv2.imwrite(('augmented_data/rotated_90/'+ fileName[0] + '_90D_' + '.png'), rotated90)
#     cv2.waitKey(10) # waits until a key is pressed
    # cv2.destroyAllWindows() # destroys the window showing image
    
    cv2.namedWindow(window_180)
    cv2.moveWindow(window_180, 380, 0)
#     cv2.imshow(window_180,rotated180)
    cv2.imwrite(('augmented_data/rotated_180/'+ fileName[0] + '_180D_' + '.png'), rotated180)
#     cv2.waitKey(10) # waits until a key is pressed
    # cv2.destroyAllWindows() # destroys the window showing image
    
    cv2.namedWindow(window_270)
    cv2.moveWindow(window_270, 380, 370)
#     cv2.imshow(window_270,rotated270)
    cv2.imwrite(('augmented_data/rotated_270/'+ fileName[0] + '_270D_' + '.png'), rotated270)
#     cv2.waitKey(1000) # waits until a key is pressed
#     cv2.destroyAllWindows() # destroys the window showing image


def main(args):
    fileName = str(args[1])
    input_net = open(fileName)
    
    for line in input_net:
        aux = line.split('\n')
        imageName = aux[0]
        print(imageName)
        rotate_image(imageName)

    input_net.close()    
    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv)) 

