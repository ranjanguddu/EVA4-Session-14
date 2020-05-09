# S14-15: Creation of A Very Large Dataset

This Repo explains how you can, not just use available datasets in your journey of DNN but efficiently create them yourself.

## Description  
We have used approximately 100 background images and 100 foreground objects to create a massive dataset with more than 400,000 images.  
Also, corresponding masks for each resultant as well as foreground objects has been created.  
We ultimately create depth maps of all images in our dataset.  
A special focus has been laid on to handling such massive size of data efficiently with limited resources.

## Starting with..
### Background  
Background contains pictures of empty roads of all sorts, ranging from city roads to flyovers. 

<b>Specifications</b>  
1. Image dimensions: 224\*224 pixels  
2. Image format: jpg - We take a special care to avoid png format here in order to save space.  
3. Number of Images: 115  

<p float="left">
  <img src="/background/S_50.jpg" width="150" />
  <img src="/background/S_3.jpg" width="150" /> 
  <img src="/background/S_73.jpg" width="150" />
  <img src="/background/S_102.jpg" width="150" />
  <img src="/background/S_57.jpg" width="150" />
</p>

### Foreground  
Foreground contains object as car on a transparent background in all possible orientations.  

<b>Specifications</b>  
1. Image dimensions: varies from 94px to 120px (aspect ratio maintained to fit background)
2. No.of channels: 4
3. Image format: png - preserves the alpha channel(transparency)
4. Number of Images: 200 (100 non-flipped + 100 horizontal flipped)

<p float="left">
  <img src="/foreground/Car_0.png" width="100" />
  <img src="/foreground/Car_73.png" width="100" /> 
  <img src="/foreground/Car_23.png" width="100" />
  <img src="/foreground/Car_186.png" width="100" />
  <img src="/foreground/Car_75.png" width="100" />
  <img src="/foreground/Car_19.png" width="100" />
  <img src="/foreground/Car_70.png" width="100" />
  <img src="/foreground/Car_83.png" width="100" />
</p>  

### Masks
<b>Foreground </b>

