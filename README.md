This program is activated by running the "AI_main_.py" file, and the result gets saved as "image.jpg". 
If you wish to save this, either change the file name or move the file to another PATH (preferrably the Results folder).

This program has some requirements. Firstly, it requires the python PIP addon, which can be installed by running the "Install PIP.bat" file.
When this program is finished running, start the "get-pip.py" file appearing, and wait until completion.
After PIP is installed, run the "Install lib.bat" file to install the modules required.

If this still doesn't work, change the file extension of "Install PIP" and "Install lib" from .bat to .txt, and write each line of the files manually into the command line.
The command line is opened by pressing the windows key, writing "cmd", and running the program appearing.
After all this is done, and verified that the program is working, you can delete these files.




The ONLY variables that should be changed by the user, is the Image_Source, T_Weight, Width and Height variables in "var.txt".
Image_Source describes the file name of an image in the IMG_SRC folder, and can be changed to any other image (preferrably .jpg file).
T_Weight decides how much the image source should affect the result, with values ranging between 0 and 1. 
Width and Height is the dimensions of the product image.

DO NOT change, delete, open or in any way affect the files in the SRC folder, as these contain the files required to create the images.
Opening or unzipping these may lead to overheating of the computer, or corruption of data.

PS: If it still doesn't work, open the "ART_Core.py" file, and remove the following text, located in the top:
from PIL import Image
def Show():
    im = Image.open(r"{}\image.jpg".format(PATH)) 
    im.show() 


After this the image won't automatically pop up on the screen, but it will still be saved as "image.jpg".