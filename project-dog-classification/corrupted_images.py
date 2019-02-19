# https://study-hall.udacity.com/rooms/community:nd101:633452-project-300/community:thread-11896069198-454018?contextType=room

import os
import glob 
from PIL import Image 
from PIL import ImageFile 
ImageFile.LOAD_TRUNCATED_IMAGES = False

image_paths = glob.glob('dogImages/train/098.Leonberger/*.jpg')

for i in range(len(image_paths)): 
    im = Image.open(image_paths[i]) 
    try: 
        im.save("temp.jpg") 
    except: 
        print("Corrupt image: ",image_paths[i]) 
        ImageFile.LOAD_TRUNCATED_IMAGES = True 
        im.save(image_paths[i]) 
        ImageFile.LOAD_TRUNCATED_IMAGES = False