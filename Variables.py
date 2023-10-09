 
file = open('var.txt') 
 
content = file.readlines()

def Source_v():
    Image_Source =(content[1])
    return Image_Source

def Weight_v():
    T_Weight = (content[3])
    return T_Weight

def Width_v():
    Width = (content[5])
    return Width

def Height_v():
    Height = (content[7])
    return Height

