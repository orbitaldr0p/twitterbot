from PIL import Image
import random
import os
from datetime import datetime

def get_white_noise_image(width, height):
    pil_map = Image.new("RGBA", (width, height), 255)
    random_grid = map(lambda x: (
            int(random.random() * 256),
            int(random.random() * 256),
            int(random.random() * 256)
        ), [0] * width * height)
    pil_map.putdata(list(random_grid))
    path = "whitenoise.png"
    pil_map.save(path)
    return path
