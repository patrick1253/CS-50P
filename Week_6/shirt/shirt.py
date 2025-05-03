# CS50 assignment:  see https://cs50.harvard.edu/python/2022/psets/6/shirt/ for full (lengthy) description
# of this assignment.

    #Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, 
    
    #resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/
    #ImageOps.html#PIL.ImageOps.fit, 
    
    #using default values for method, bleed, and centering, overlay the 
    #shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, 
    #and 
    
    #save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.


import sys
from PIL import Image, ImageOps

def main():
    filename = sys.argv[1:]
    
    if len(filename) < 2:
        sys.exit("Too few CLI arguments")

    if len(filename) > 2:
        sys.exit("Too many CLI arguments")

    suffix0 = (filename[0].split('.')[-1]).lower()
    suffix1 = (filename[1].split('.')[-1]).lower()

    if suffix0 not in ["png", "jpg", "jpeg"]:
        sys.exit(f"\"{filename[0]}\" is not a png, jpg, or jpeg filename")

    if suffix1 != suffix0:
        sys.exit(f"\"{filename[0]}\" and \"{filename[1]}\" must have the same extension: png, jpg, or jpeg")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print(input_file, output_file)

    try:
        file = open(input_file, "r")
    except FileNotFoundError:
        sys.exit(f"\"{input_file}\" does not exist")
    else:
        shirt = Image.open("shirt.png")
        size = shirt.size
        photo = Image.open(input_file)
        photo = ImageOps.fit(photo, size = (size), method = 0, bleed = 0.0, centering =(0.5, 0.5))
        photo.paste(shirt, shirt)
        photo.save(output_file)


if __name__ == "__main__":
    main()
