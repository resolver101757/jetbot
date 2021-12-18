import time
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_bus=1, gpio=1) # setting gpio to 1 is hack to avoid platform detection

while True:
    
    try:
        # Try to connect to the OLED display module via I2C.
        disp.begin()
    except OSError as err:
        print("OS error: {0}".format(err))
        time.sleep(10)
    else:
        break

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

def execute_command(bash_command):
    """runs a bash command and returns the output as a string

    Args:
        bash_command ([type]): bash command to run as a string

    Returns:
        [type]: returns the output of the bash command as a string
    """       
    cmd = bash_command
    command = subprocess.check_output(bash_command, shell = True )
    return command 

def write_to_screen(line1, line2, line3, line4):
    """writes data to the 128 by 128 lcd screen using the Adafruit library
    
    It contains 4 lines of text, each line is a string of up to 21 characters long

    Args:
        line1 ([type]): 1st line, any string of up to 21 characters long
        line2 ([type]): 2nd line, any string of up to 21 characters long
        line3 ([type]): 3rd line, any string of up to 21 characters long
        line4 ([type]): 4th line, any string of up to 21 characters long
    """    
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)


    # Write two lines of text.
    draw.text((x, top),       line1, font=font, fill=255)
    draw.text((x, top+8),     line2, font=font, fill=255)
    draw.text((x, top+16),    line3, font=font, fill=255)
    draw.text((x, top+25),    line4, font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()