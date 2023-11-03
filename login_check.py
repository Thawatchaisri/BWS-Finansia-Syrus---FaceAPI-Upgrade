from base64 import b64decode
from deepface.DeepFace import verify, build_model
from time import time
from os import remove

def login_check(uid, image):
    file_new = str(time())
    header, encoded = image.split(',', 1)
    with open(file_new + '.png', 'wb') as (f):
        f.write(b64decode(encoded))

    try:
        results = verify(img1_path = file_new + '.png' , img2_path = 'student/' + uid + '.png',model_name = 'VGG-Face', detector_backend = 'fastmtcnn',enforce_detection =True)
        if results['verified']:
            remove(file_new +'.png')
            return 'Match'
        else:
            remove(file_new+'.png')
            return 'Not match'
    except:
        remove(file_new + '.png')
        return 'No face detected'       