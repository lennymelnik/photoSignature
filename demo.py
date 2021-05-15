from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np
import math
import pandas as pd

from flask import Flask, jsonify
app = Flask(__name__)
img = Image.open('download.jpeg', 'r').convert("RGB")
im_matrix = np.array(img)
print(im_matrix)




def print_in_color(txt_msg,fore_tupple,back_tupple,):
    #prints the text_msg in the foreground color specified by fore_tupple with the background specified by back_tupple 
    #text_msg is the text, fore_tupple is foregroud color tupple (r,g,b), back_tupple is background tupple (r,g,b)
    rf,gf,bf=fore_tupple
    rb,gb,bb=back_tupple
    msg='{0}' + txt_msg
    mat='\33[38;2;' + str(rf) +';' + str(gf) + ';' + str(bf) + ';48;2;' + str(rb) + ';' +str(gb) + ';' + str(bb) +'m' 
    return msg, mat
    
    #print('\33[0m') # returns default print color to back to black

# example of use using a message with variables


fore_color='cyan'
back_color='dark green'
msg='foreground color is {0} and the background color is {1}'.format(fore_color, back_color)
for x in range(0,len(im_matrix)):
    for i in range(0,len(im_matrix[x])):    
        msg, mat = print_in_color('l', (255,255,255),(im_matrix[x][i][0],im_matrix[x][i][1],im_matrix[x][i][2]))
        print(msg .format(mat), end =" ")
    print('')


'''
for x in range(0,len(im_matrix)):
    for i in range(0,len(im_matrix[x])):    
        print(str(im_matrix[x][i]), end =" ")
    print('')
'''
