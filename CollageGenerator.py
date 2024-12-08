from PIL import Image
from tkinter import filedialog
import random

# Adds to the denomonator when calculating the average height of images on a line
AVG_Y_BIAS = 1

# Devides the numerator by a specified amount when calculating average height of a line
TOTAL_Y_BIAS = 1.5

# Value to rotate all images (random number between -ROTATE_VALUE and ROTATE_VALUE)
ROTATE_VALUE = 10

# Fraction of image that the image can move in up and to the left
FRACTION_OF_IMAGE_TO_SHAKE_X = 2
FRACTION_OF_IMAGE_TO_SHAKE_Y = 2

# Width and height of final image
WIDTH = 816 * 10
HEIGHT = 1056 * 10

# Create final image
image = Image.new(mode = "RGBA", size = (WIDTH,HEIGHT))

# Set up variables
position = [0,0]
totalY = 0
numImages = AVG_Y_BIAS
avgY = 0

files = filedialog.askopenfilenames(filetypes =[("image", ".jpeg"), ("image", ".png"),("image", ".jpg"),])
filesList = list(files)
random.shuffle(filesList)

for file in filesList:

    with Image.open(file).convert("RGBA") as im:
        if(position[0] > WIDTH):
            position[0] = 0
            position[1] += int(avgY / TOTAL_Y_BIAS)
            avgY = 0
            numImages = AVG_Y_BIAS
            totalY = 0

        im = im.rotate(random.randint(ROTATE_VALUE*-1,ROTATE_VALUE), expand=True)

        offset = [
            random.randint(int(im.size[0]/FRACTION_OF_IMAGE_TO_SHAKE_X*-1), 0) ,
            random.randint(int(im.size[1]/FRACTION_OF_IMAGE_TO_SHAKE_Y*-1), 0)
            ]

        image.paste(im,(position[0] + offset[0] ,position[1] + offset[1]), mask=im)

        position[0] += im.size[0] + offset[0]
        numImages += 1
        totalY += im.size[1]
        avgY = int(totalY / numImages)
    
image = image.convert("RGB").save(str(filedialog.askdirectory()) + "\\" + input("filename: ") + ".jpg")
