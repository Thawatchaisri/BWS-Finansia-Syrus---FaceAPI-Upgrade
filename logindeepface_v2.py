from base64 import b64decode
#import face_recognition as fr
#import time, os, pickle, glob
from deepface.DeepFace import verify, build_model
from time import time
from os import remove

def login_check(uid, image):
    #image : base64 image
    #uid : pictureID filename (jpg)
    file_new = str(time())
    header, encoded = image.split(',', 1)
    with open(file_new + '.jpg', 'wb') as (f):
        f.write(b64decode(encoded))

    try:
        results = verify(img1_path = file_new + '.jpg' , img2_path = 'student/' + uid + '.jpg',model_name = 'OpenFace', detector_backend = 'opencv',enforce_detection =True)
        if results['verified']:
            remove(file_new +'.jpg')
            return 'Match'
        else:
            remove(file_new+'.jpg')
            return 'Not Match'
    except:
        remove(file_new + '.jpg')
        return 'No face detected'       