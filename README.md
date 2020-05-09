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
4. Folder size: 1.06MB

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
5. Folder Size: 2.17MB

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

### Foreground Mask
Foreground masks have been created using the alpha channel of the png images  
<b>Specifications</b>
1. Image format: jpg
2. Number of channels: 1
3. Number of Images: 200
4. Folder size: 400KB  

<p float="left">
  <img src="/fg_mask/Car_0_mask.jpg" width="100" />
  <img src="/fg_mask/Car_73_mask.jpg" width="100" />
  <img src="/fg_mask/Car_23_mask.jpg" width="100" />
  <img src="/fg_mask/Car_186_mask.jpg" width="100" />
  <img src="/fg_mask/Car_75_mask.jpg" width="100" />
  <img src="/fg_mask/Car_19_mask.jpg" width="100" />
  <img src="/fg_mask/Car_70_mask.jpg" width="100" />
  <img src="/fg_mask/Car_83_mask.jpg" width="100" />
</p>  

### Fg_Bg Together: OverLayed Images  
Foreground objects are overlayed on each background image at 20 random positions.  
This gives a total of 115\*200\*20 = 4,60,000 images.  

Here's a peek into few of our images:  

<p float="left">
  <img src="/fg_bg/P_1.jpg" width="150" />
  <img src="/fg_bg/P_172126.jpg" width="150" />
  <img src="/fg_bg/P_100071.jpg" width="150" />
  <img src="/fg_bg/P_148576.jpg" width="150" />
  <img src="/fg_bg/P_156303.jpg" width="150" />
</p>

### Corresponding fg_bg Masks  
These masks are created by overlaying the foreground masks on a black patch of size equal to background image's size.  
The corresponding masks are:  

<p float="left">
  <img src="/fg_bg_mask/mask_1.jpg" width="150" />
  <img src="/fg_bg_mask/mask_172126.jpg" width="150" />
  <img src="/fg_bg_mask/mask_100071.jpg" width="150" />
  <img src="/fg_bg_mask/mask_148576.jpg" width="150" />
  <img src="/fg_bg_mask/mask_156303.jpg" width="150" />
</p>
