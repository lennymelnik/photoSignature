from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np
import math

import os 




def addSignature(fileName):
    img = Image.open('input/'+fileName, 'r').convert("RGB")
    grey_img = ImageOps.grayscale(img)

    img_w, img_h = img.size
    #scale the signature down
    maxsize = (img_w/3, img_h/3)
    signature = Image.open('signature.png', 'r').convert("RGBA")
    signature.thumbnail(maxsize, Image.ANTIALIAS)
    #background = Image.new('RGBA', (img_w, img_h), (177, 177, 40, 1))
    #Set the signature in the bottom right corner
    width = (img.width - signature.width) // 1
    
    height = (img.height - signature.height) // 1
    im_matrix = np.array(grey_img)
    sg_matrix = np.array(signature)
    avg_r = 0
    #avg_g = 0
    #avg_b = 0
    howMany = 0
    """
    for i in range(len(im_matrix)-len(sg_matrix), len(im_matrix)):
        for x in range(len(im_matrix[0])-len(sg_matrix[0]),len(im_matrix[0])):
            #if(list(signature.getpixel((i, j)))[3] != 0):
            #print("Color value",im_matrix[i][x])
            avg_r += im_matrix[i][x][0]#*0.2126
            avg_g += im_matrix[i][x][1]#*0.7152
            avg_b += im_matrix[i][x][2]#*0.0722
            howMany +=1
            """

    for i in range(len(im_matrix)-len(sg_matrix), len(im_matrix)):
        for x in range(len(im_matrix[0])-len(sg_matrix[0]),len(im_matrix[0])):
            #if(list(signature.getpixel((i, j)))[3] != 0):
            #print("Color value",im_matrix[i][x])
            avg_r += im_matrix[i][x]
            howMany +=1
            
    avg_r = round(avg_r/howMany)
    #avg_g = round(avg_g/howMany)
    #avg_b = round(avg_b/howMany)

    #r = max(avg_r,avg_b,avg_g) + min(avg_r,avg_b,avg_g) - avg_r   
    #b = max(avg_r,avg_b,avg_g) + min(avg_r,avg_b,avg_g) - avg_b   
    #g = max(avg_r,avg_b,avg_g) + min(avg_r,avg_b,avg_g) - avg_g   


    def hilo(a, b, c):
        if c < b: b, c = c, b
        if b < a: a, b = b, a
        if c < b: b, c = c, b
        return a + c

    def complement(r, g, b):
        k = hilo(r, g, b)
        return tuple(k - u for u in (r, g, b))

    #complementColor = list(complement(avg_r,avg_g,avg_b))
    #list(complement(avg_r,avg_g,avg_b))
    for i in range(signature.size[0]):
        for j in range(signature.size[1]):
            if(list(signature.getpixel((i, j)))[3] >= 100):
                if(avg_r >= 127):
                    signature.putpixel((i, j), (0,0,0))
                else:
                    signature.putpixel((i, j), (255,255,255))

                #signature.putpixel((i, j), (255, 255, 255))

    '''outline = signature.filter(ImageFilter.FIND_EDGES)
    for i in range(outline.size[0]):
        for j in range(outline.size[1]):
            if(list(outline.getpixel((i, j)))[3] >= 150):
                outline.putpixel((i, j), (avg_r,avg_g,avg_b, 100))
                #signature.putpixel((i, j), (255, 255, 255))'''

    #outline.show()
    obj = ImageEnhance.Brightness(signature)
    signature = obj.enhance(1.2)
    img.paste(signature, (width, height), signature)
    #img.paste(outline, (width, height), outline)

    img.save('output/'+fileName)



path = os.getcwd()+'/input' 
files = os.listdir(path)  
for f in files:
    if(f.split('.')[1] == 'png' or f.split('.')[1] =='jpg' or f.split('.')[1] =='jpeg'): 	
        print(f.split('.')[1] == 'jpg')
        addSignature(f)


