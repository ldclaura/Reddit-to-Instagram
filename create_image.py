# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('images.png') #replace with something a bit nicer.
#and probably a bigger image NOTE NOTE NOTE <<<

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.load_default()

# Add Text to an image
I1.text((10, 10), "Nice Car", font=myFont, fill =(255, 0, 0))

# Display edited image
img.show()

# Save the edited image
img.save("car2.png")