from base64 import b64decode
from deepface.DeepFace import verify
from time import time
from os import remove

def login_check(uid, image):
    file_new = str(time())
    _, encoded = image.split(',', 1)
    with open(file_new + '.png', 'wb') as (f):
        f.write(b64decode(encoded))

    try:
        results = verify(img1_path = file_new + '.png' , img2_path = 'student/' + uid + '.png',model_name = 'Facenet', detector_backend = 'ssd',enforce_detection =True)
        if results['verified']:
            remove(file_new +'.png')
            return 'Match'
        else:
            remove(file_new+'.png')
            return 'Not match'
    except:
        remove(file_new + '.png')
        return 'No face detected'       