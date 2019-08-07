# Grid_Maker
This program makes a grid of heterogeneous images with flexibility and labels the image if required. 

This is a python program which takes hetrogeneous images annd curates a grid of of dimensions chosen by the user. You can change the resolution,aspect ratio of a single image in the grid.
If needed, you can add text in the images with a font of your choice. 

Compatibility - Python 3
Preferable - Create a virtual environment to work on so that the installed programs don't meddle with past or future versions. I prefer virtualenv to do this.

Steps to run the program:

- Put all the images in a folder 
- Clone the repository and navigate to the respective folder
- Run the following command on terminal - pip install -r requirements.txt   
- If label needs to be added to the images, download the .tff file of your favorite format.
- Run the program with the respective arguments - 
  python make_grid.py -image_folder /home/rachna/images -gridname /home/anil/grid -keeplabel true
- Following are the arguments you can set.
   -image_folder,-resolution,-aspect_ratio,-grid_dim,-keeplabel,-fontpath,-imageformat, -gridname,
   -fontsize 
  
- tff file of Times New Roman has been given in the repo as an example

Here is a result with default settings

![alt text](https://github.com/Rachquazar/Grid_Maker/blob/master/images/grid.png)
