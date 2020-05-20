import cv2
import os

for root, dirs, files in os.walk('/Users/nove/breast_cancer_analyzer_LCAD/src/mammo_preprocessing/normalize'):
    it = 0
    for i, f in enumerate(files):
        img = cv2.imread(root + '/' + f)
        imgAux = img[:, :img.shape[1], :]

        if ((imgAux == 0).sum() > 9):
            fname = root + '/' + f
            imgRename = cv2.imread(fname)
            cv2.imwrite('trash' + it, imgRename)
            it+=1
            del imgRename
        del img