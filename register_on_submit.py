from base64 import b64decode
from deepface.DeepFace import detectFace
from os import remove

def register_on_submit(email, image):
    """
    The function `register_on_submit` takes an email and an image as input, saves the image as a file,
    detects the face in the image, and returns a success message if the face is detected or a failure
    message if the face cannot be detected.
    
    :param email: The email parameter is a string that represents the email address of the user who is
    registering
    :param image: The "image" parameter is a base64 encoded string representation of an image
    :return: The function `register_on_submit` returns a string. If the face in the image can be
    detected, it returns the message "Registration successful!". If the face cannot be detected, it
    returns the message "Registration failed! Cannot detect your face. Please try again."
    """
    _, encoded = image.split(',', 1)
    file_new = email
    
    with open('student/' + file_new + '.png', 'wb') as (f):
        f.write(b64decode(encoded))
    try:
       detectFace('student/'+file_new +'.png') 
       return 'Registration successful!'
    except:
        remove('student/' + file_new + '.png')
        return 'Registration failed! Cannot detect your face. Please try again.'
