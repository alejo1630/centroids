# Centroids Tool

With this Python code it's possible to find the centroid of a regular or irregular geometric figures wich are solid or have holes, using [Open CV library](https://opencv.org/)

## 🔰 How does it work?
- User has to include a image (JPG, PNG, etc) in the folder **Figures**.
- The image must be line based figure where the background is clear or white, and the figure has black solid lines. Such as:

<img src = "https://github.com/alejo1630/centroids/blob/main/Image_Readme/1.JPG" width="400" >

- After run the code, the user has to input the name of the file using the console.
- The image will appear in a a popup window.
- The user has to use the right click to select the reference origin. A red dot will appear in tha position

<img src = "https://github.com/alejo1630/centroids/blob/main/Image_Readme/2.png" width="400">

- This reference origin will be used to define the centroid's coodinates
- After set the reference origin the user has to select another point to create a straight line. The current code is based on X direction but it could be modify to Y direction in line 61.

<img src = "https://github.com/alejo1630/centroids/blob/main/Image_Readme/3.png" width="400">

 - The code uses the distance between the reference origin and the second point to have a reference value to convert the pixel information into distance measurement units such as cm, inches etc.
 - The user must be knonw the real distance (cm, inches, etc) between the reference origin and the second point. This value will be inputted using the console to convert the pixel units. 
 - With this information the code calculates de centroid using distance measurement units, the figure's contours and the [moments](https://www.pythonpool.com/opencv-moments/) of all the pixels which define the figure.
 - In this example the line of reference has a real length of 20 mm, with this information the calculated centroid is:
 
 $$ x = 144.88 mm$$
 
 $$ y = 97.56 mm $$
  
 <img src = "https://github.com/alejo1630/centroids/blob/main/Image_Readme/4.png" width="400">
 
- The real centroid of the figure used in the example is $x = 145.09 mm$ and $y = 96.86mm$. This means an error of less of **1%** in the calculation of centroids in both x and y direction.
  
## 🔶 What is next?
- Calculate the centroid of geometric figures in recorded or live videos.
