# CS50 assignment:  In a file called shirtificate.py, implement a program that prompts the user for 
# their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar 
# to this one for John Harvard, with these specifications:

#    The orientation of the PDF should be Portrait.
#    The format of the PDF should be A4, which is 210mm wide by 297mm tall.
#    The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
#    The shirt’s image should be centered horizontally.
#    The user’s name should be on top of the shirt, in white text.

# All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your 
# shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

# Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s 
# API (application programming interface) to see all of its functions and parameters therefor.


from fpdf import FPDF
from PIL import Image, ImageOps

class PDF():
    def __init__(self, prompt):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", style="B", size=50)

        # Change color of header text (default = black)         
        # self._pdf.set_text_color(100, 250, 50)

        self._pdf.cell(0, 60, 'CS50 Shirtificate', border = 0, align = 'C')
        
        self._pdf.image("shirtificate.png", x = 10, y = 80, keep_aspect_ratio=True, w =190) # x=self._pdf.epw * 0.1, y=60, k, w=self._pdf.epw * 0.9)
        
        image_size = Image.open("shirtificate.png").size
        #print(image_size)

        # Change color, size of t-shirt text
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font_size(30)

        text = f"{prompt} took CS50"
        #self._pdf.text(x = 60, y = 140, text = text)
        self._pdf.cell(0, 260, text = text, align = "C", center=True)
        
        self._pdf.output("patrick_shirt.pdf")

def main():
    prompt = input("Name: ")
    pdf = PDF(prompt)


if __name__ == "__main__":
    main()
    


'''
    #file = open(shirtificate.png, "r")
    shirt = Image.open("shirtificate.png")
    size = shirt.size
    photo = Image.open(input_file)
    photo = ImageOps.fit(photo, size = (size), method = 0, bleed = 0.0, centering =(0.5, 0.5))
    photo.paste(shirt, shirt)
    photo.save('shirtificate2.png')
'''
