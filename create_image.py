# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('images.png') #replace with something a bit nicer.
#and probably a bigger image NOTE NOTE NOTE <<<
width, height = img.size
print(width)
print(height)
padding = width/8

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype("LoveDays-2v7Oe.ttf", 225)

text = """The teenager,
                   who has been searching for over a year for casual,
                   no-experience-required work in the Bendigo area (excluding Maccas/KFC/HJ),
                   received several promising leads. The most viable avenues to pursue,
                   based on the community's suggestions and the teenager's positive responses, are:"""

# Add Text to an image

# Function to wrap text to fit image width
def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        # Try adding the next word
        test_line = current_line + word + " "
        # Measure line width
        line_width = I1.textlength(test_line, font=font)
        if line_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.rstrip())
            current_line = word + " "
    lines.append(current_line.rstrip())
    return "\n".join(lines)

max_text_width = width - (2*padding)
# Wrap text to image width (with some padding)
wrapped_text = wrap_text(text, myFont, max_text_width)

# Draw wrapped text
I1.multiline_text((padding, height/8), wrapped_text, font=myFont, fill="#b585bc", spacing=10)



# Display edited image
img.show()

# Save the edited image
img.save("test.png")
