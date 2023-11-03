from base64 import b64decode
from deepface.DeepFace import detectFace
from os import remove

def register_on_submit(email, image):
    header, encoded = image.split(',', 1)
    file_new = email
    
    with open('student/' + file_new + '.png', 'wb') as (f):
        f.write(b64decode(encoded))
    try:
       detectFace('student/'+file_new +'.png') 
       return 'Registration Successful!'
    except:
        remove('student/' + file_new + '.png')
        return 'Registration failed! Cannot detect your face. Please try again.'
