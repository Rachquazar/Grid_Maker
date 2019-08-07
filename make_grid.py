#Run the command - pip install -r requirements.txt

import cv2
import os
import numpy as np
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Image grid maker')

#Either pass arguments on terminal or change values here

parser.add_argument('-image_folder', default='/home/anil/Desktop/images')
parser.add_argument('-resolution', default = 128,type=int)
parser.add_argument('-aspect_ratio', default='4:3',type=str)
parser.add_argument('-grid_dim', default='1:6', type=str)
parser.add_argument('-keeplabel', default='true')
parser.add_argument('-fontpath', default='/home/anil/Desktop/Times New Roman.ttf', type=str)
parser.add_argument('-imageformat', default='png', type=str)
parser.add_argument('-gridname', default='/home/anil/Desktop/grid', type=str)
parser.add_argument('-fontsize', default=80, type=int)

args = parser.parse_args()


font_path = args.fontpath
format_label = args.imageformat
aspect_ratio_x = int(args.aspect_ratio[0])
aspect_ratio_y = int(args.aspect_ratio[2])
path = args.image_folder
aspect_ratio = [aspect_ratio_x,aspect_ratio_y] 
resolution = args.resolution   #how clear the image will be
image_name = args.gridname
keeplabel = args.keeplabel

image_list = os.listdir(path)

aspect_ratio = [aspect_ratio_x,aspect_ratio_y] 
resolution = args.resolution   #how clear the image will be

  
number_of_images_in_a_column = int(args.grid_dim[2])
number_of_images_in_a_row = int(args.grid_dim[0])

height = number_of_images_in_a_row
width = number_of_images_in_a_column

h = resolution*aspect_ratio[0]  #height of one image in the grid
w = resolution*aspect_ratio[1]  #width of one imagein the grid

a = width*w
b = height*h
c = 3       #number of channels in the images

grid_shape = (a,b,c)

i=0
j=0

grid = np.zeros(grid_shape)

fontsize = 80
font = ImageFont.truetype(font_path, fontsize)


alphabet = 'abcdefghijkl'
alpha=0

for image in image_list:
   
  new_im = Image.open(path +'/'+ image)
  
  text = '('+alphabet[alpha]+')'
  alpha = alpha+1 
  if keeplabel=='true':

    draw = ImageDraw.Draw(new_im)
    # Chnage the font colour by changing the values of (0,0,0). All three of the values can be varied from 0 to 255
    draw.text((0, 0),text,(0,0,0),font=font)   
 
  new_im = np.array(new_im,dtype=np.float32)
  new_im = cv2.resize(new_im,(h,w))
  new_im = cv2.cvtColor(new_im,cv2.COLOR_RGB2BGR)
  
  if j<a:
    if i>=b:
      i = 0
      j = j+w
    grid[j:j+w, i:i+h] = new_im
    i = i+h


print ('Size of final image', grid.shape)
cv2.imwrite(image_name+'.'+format_label,grid)
print ('Grid has been saved at '+image_name+'.'+format_label)
