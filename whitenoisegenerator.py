from PIL import Image
import random
import os
from datetime import datetime
# generates the white noise, returns the file path to the image
def get_white_noise_image(width, height):
    pil_map = Image.new("RGBA", (width, height), 255)
    # uses a lambda function to randomly generate RGB colour code
    # it takes the colour codes and replaces each value in an array of 0s with the colour code
    random_grid = map(lambda x: (
            int(random.random() * 256),
            int(random.random() * 256),
            int(random.random() * 256)
        ), [0] * width * height)
    # adds the data to the image and saves it as whitenoise.png
    pil_map.putdata(list(random_grid))
    path = "whitenoise.png"
    pil_map.save(path)
    return path
