from base64 import b64decode
#import face_recognition as fr
#import time, os, pickle, glob
from deepface.DeepFace import verify, build_model
from time import time
from os import remove

def login_check(uid, image):
    #image : base64 image
    #uid : pictureID filename (png)
    face_match = 0
    file_new = str(time())
    header, encoded = image.split(',', 1)
    with open(file_new + '.png', 'wb') as (f):
        f.write(b64decode(encoded))

    try:
        results = verify(img1_path = file_new + '.png' , img2_path = 'student/' + uid + '.png',detector_backend = 'retinaface',model = build_model('VGG-Face'), prog_bar = False,enforce_detection =True)
      
        if results['verified']:
            # remove(file_new +'.png')
            return 'Match'
        else:
            # remove(file_new+'.png')
            return 'Not Match'
    except:
        # remove(file_new + '.png')
        return 'No face detected'       