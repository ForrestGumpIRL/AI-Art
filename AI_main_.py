import ART_Core

import pathlib

import random

import Variables


Image_Source = str(Variables.Source_v())
Image_Source = Image_Source.strip()




PATH = pathlib.Path(__file__).parent.resolve()


Continue = "y"

while Continue == "y":

    is_str = False
    
    style = input("""Which style do you want to use? (type "?" for list of available styles)\n""")

    try:
        style = int(style)
        is_str = False
        is_int = True
        
        
    except:

        is_str = True
        is_int = False

    while is_str == True:

        try:
            style = int(style)
            is_str = False
            is_int = True
        
        
        except:
            is_str = True
            is_int = False


        
        if style == "?":
            f = open('src.txt', 'r')
            file_contents = f.read()
            print (file_contents)
            f.close()
            style = input("""Which style do you want to use? (type "?" for list of available styles)\n""")

        elif is_int == False and style != "?":
            print("The style has to be one of the numbers listed! ")
            style = input("""Which style do you want to use? (type "?" for list of available styles)\n""")

        elif style == 0:
            style = random.randint(1,116)
            print("The random style chosen was: {}".format(style))
            is_str = False

        else:
            style = int(style)
            is_str = False

    if style == 0:
        style = random.randint(1,116)
        print("The random style chosen was: {}".format(style))
        is_str = False

    elif style == -1:
        style = random.randint(76,116)
        print("The random style chosen was: {}".format(style))
        is_str = False


    else:
        style = int(style)
        is_str = False


    prompt = input("And what is the prompt? (what the image should portray) \n")

    use_img = input("Do you want to use the input image? (y/n) \n")

    if use_img == "y" or use_img == "yes" or use_img == "Y":
        use_img = True
    else:
        use_img = False

    image_path = "{}/IMG_SRC/".format(PATH)

    image = image_path + Image_Source

    if use_img == True:
        ART_Core.send_task_to_image_gen(style, prompt, image)
        

    else:
        ART_Core.send_task_to_image_gen(style, prompt)

    Continue = input("Do you want to retry? (y/n) \n")



