# NeuralStyleTransfer-Flask
### BEFORE RUNNING: open config.py edit the UPLOAD_FOLDER path to wherever you downloaded the project to. 

### You can easily get the path by clicking the path in a file explorer (windows): 
![image](https://user-images.githubusercontent.com/91845564/234740027-218c20f7-4105-430a-86e5-5f2ac1994245.png)

### MAKE SURE to change the '\\' to '/' and that the last folder is 'static'.

## Neural Style Transfer
#### This implementation of Neural Style Transfer uses the GATYS model. I have edited the code from https://pytorch.org/tutorials/advanced/neural_style_tutorial.html to work with flask.
#### When first running it will download the models. When running the style transfer it will use your GPU if cuda is available, otherwise it will use your CPU. Only the following NVIDIA GPU's have cuda: https://developer.nvidia.com/cuda-gpus

## Starting from the home page you can login, register or logout:
![image](https://user-images.githubusercontent.com/91845564/234736967-eff8ff91-c46b-4e2a-800c-c19fc37e5f3b.png)

## The Photos tab is where you choose which images for the style transfer. The content image will be the base and style image will be the style you want to apply. Strength is the number of iterations.
![image](https://user-images.githubusercontent.com/91845564/234740380-97382134-64fd-4d34-b012-6235b05d7a1a.png)

## The '/result' page displays the output of the style transfer along with the inputs below.
![image](https://user-images.githubusercontent.com/91845564/234741555-0326f865-c5f0-48f8-9359-e1f5892b04a1.png)

## The Examples tab is where you can download some example images to use if you don't want to use your own.
#### If your computer doesn't have images that you would like to use, try opening the website on your phone.
![image](https://user-images.githubusercontent.com/91845564/234740648-fad62a4a-bbc4-4b70-a3e7-cbe41e333570.png)
## To download simply right click an image and choose 'Save Image As'.
![image](https://user-images.githubusercontent.com/91845564/234741905-26dba431-a943-4e91-8c74-a7233d6c26d8.png)


## The Profile tab is where you can view the most recent style transfer alongside another way to view the example images.
![image](https://user-images.githubusercontent.com/91845564/234741934-b443ec65-d855-4480-ae20-c729992e8c59.png)

## When creating a virtual environment
### Flask-Navigation may not work, in that case you will need to edit the following files:
#### item.py
#### navbar.py
#### Located at: venv\Lib\site-packages\flask_navigation\
### I have included the correct version in the folder \flask-navigation-files

