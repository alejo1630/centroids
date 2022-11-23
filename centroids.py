### Load libraries
import cv2

#------------------------------------------------------------------------#

### Upload image

name = input("Ingrese el nombre del archivo: ")
filename = "Figures/" + name + ".jpg"
img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE) #Gray-scale figure
img_c = cv2.imread(filename) # Color Figure

#------------------------------------------------------------------------#

### Show Figure Function

def show_image(img):
	cv2.imshow("Imagen",img) #Create and show figure
	cv2.waitKey(0) # Show an static image
	cv2.destroyAllWindows() # Clase all the windows

#------------------------------------------------------------------------#

### Coordinates

def mouse_callback(event,x,y,flags,params): # Function to get coordinates
	if event == 2:
		global right_clicks, filename
		right_clicks.append([x,y])
		img_color = cv2.imread(filename)
		cv2.circle(img_color, (x,y), radius = 6, color = (0,0,255), thickness = -1)
		if len(right_clicks)> 1:
			cv2.line(img_color, tuple(right_clicks[0]),tuple(right_clicks[1]), color = (0, 0, 255), thickness = 2)

		cv2.imshow("Imagen",img_color)

right_clicks = list() # Empty list to save coords

cv2.imshow("Imagen",img) # Show image

cv2.setMouseCallback("Imagen",mouse_callback) # Call function mouse callback

cv2.waitKey(0) # Show an static image
cv2.destroyAllWindows() # Clase all the windows

#------------------------------------------------------------------------#

### Setting origin

d_x = right_clicks[0][0]
d_y = right_clicks[0][1]

#------------------------------------------------------------------------#

### Units Convert

## Size Image
height = img.shape[0]
width = img.shape[0]

dire = "X" # Reference direction

real = int(input("Ingrese la medida de referencia: ")) # Real measurament 

if dire == "X":
	conv = real/(abs(right_clicks[0][0]-right_clicks[1][0]))
else:
	conv = real/(abs(right_clicks[0][1]-right_clicks[1][1]))


#------------------------------------------------------------------------#

### Color the shape with black

## Threshold white and black
lim = 120 # Gray scale minimun value to convert it into white
white = 255 # White gray scale value 

## Binary Thrershold (black and white)
ret, img2 = cv2.threshold(img, lim, white, cv2.THRESH_BINARY) 

## Find Contours
# img2 is the image with the threshold process
# cv2.RETR_TREE is the type of hierarchy
# cv2.CHAIN_APPROX_SIMPLE is the way to store the data points of the contours
# hierarchy [Next, Previous, First_Child, Parent]
contours, hierarchy  = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = contours[1:len(contours):2] # The shape contour is selected

## Fill the contour to black
img3 = cv2.fillPoly(img_c, c, color=(0,0,0))

#------------------------------------------------------------------------#

### Find the contour and centroid

## Cambio del espacio de color
img4 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

## Find the limit between white and black
ret2,thresh = cv2.threshold(img4,127,255,cv2.THRESH_BINARY_INV)

## Contour of the black shape
contours2, hierarchy2  = cv2.findContours(img4, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

## Draw the countours
# img_c is color image
# countours is the data points of the contours
# -1 draw all the contours
# (0,255,0) color
# 2 is the width
img5 = cv2.drawContours(img_c, contours2[1:], -1, (0,255,0), 2)

## Moments calculation
M = cv2.moments(thresh)

## X and Y Coordinates in pixels
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

## X and Y Coordinates in units
cx_r = (cx-d_x)*conv
cy_r = (d_y-cy)*conv

## Plot of the centroid and coordinate
cv2.circle(img_c,(cx,cy), 5,(0,0,255),-1)
cv2.putText(img_c,"({:.2f}, {:.2f})".format(cx_r,cy_r),(cx-50,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)
show_image(img5)




