from base64 import b64decode
from deepface.DeepFace import verify
from time import time
from os import remove

def login_check(uid, image):
    """
    The function `login_check` takes a user ID and an image, saves the image as a PNG file, verifies it
    against a reference image using a face recognition model, and returns whether the images match or
    not.
    
    :param uid: The `uid` parameter is the user ID, which is used to locate the image file of the user
    in the `student` directory
    :param image: The "image" parameter is a base64 encoded string representation of an image
    :return: The function `login_check` returns one of the following strings:
    - "Match" if the image provided matches the image associated with the given `uid`.
    - "Not match" if the image provided does not match the image associated with the given `uid`.
    - "No face detected" if no face is detected in the provided image.
    """
    file_new = str(time())
    _, encoded = image.split(',', 1)
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