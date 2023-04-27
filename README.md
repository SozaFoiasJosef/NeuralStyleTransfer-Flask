# NeuralStyleTransfer-Flask
BEFORE RUNNING: open config.py edit the UPLOAD_FOLDER path to wherever you downloaded the project to. 

You can easily get the path by clicking the path in a file explorer (windows): ![image](https://user-images.githubusercontent.com/91845564/234740027-218c20f7-4105-430a-86e5-5f2ac1994245.png)

MAKE SURE to edit '/' to '\' and that the last folder is 'static'.

This implementation of Neural Style Transfer uses the GATYS model. I have edited the code from https://pytorch.org/tutorials/advanced/neural_style_tutorial.html to work with flask.
When first running it will download the models. When running the style transfer it will use your GPU if cuda is available, otherwise it will use your CPU. Only the following NVIDIA GPU's have cuda: https://developer.nvidia.com/cuda-gpus

Starting from the home page you can login, register or logout:
![image](https://user-images.githubusercontent.com/91845564/234736967-eff8ff91-c46b-4e2a-800c-c19fc37e5f3b.png)

The Photos tab is where you choose which images for the style transfer. The content image will be the base and style image will be the style you want to apply. Strength is the number of iterations.
![image](https://user-images.githubusercontent.com/91845564/234740380-97382134-64fd-4d34-b012-6235b05d7a1a.png)

The Examples tab is where you can download some example images to use if you don't want to use your own.
![image](https://user-images.githubusercontent.com/91845564/234740575-6d9e78cf-c309-4858-a05e-dd4321407c7d.png)

