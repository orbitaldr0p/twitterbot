from credentials import *
import os
from time import sleep
from authentication import connect
from whitenoisegenerator import get_white_noise_image as whitenoise

def tweet():
    api = connect(credentials['consumer_key'], credentials['consumer_secret'], credentials['access_token'], credentials['access_secret'])
    while True:
        path = whitenoise(500, 500)
        try:
            api.update_with_media(path)
            print("successfully sent")
            os.remove(path)
        except:
            print("Sending Failed")
        sleep(3600)
tweet()