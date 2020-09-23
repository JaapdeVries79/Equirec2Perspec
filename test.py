import os
import cv2 
import Equirec2Perspec as E2P


equ = E2P.Equirectangular('src/test1.JPG')    # Load equirectangular image

# FOV unit is degree 
# theta is z-axis angle(right direction is positive, left direction is negative)
# phi is y-axis angle(up direction positive, down direction negative)
# height and width is output image dimension 

img = equ.GetPerspective(120, 180, -15, 720, 1080) # Specify parameters(FOV, theta, phi, height, width)

# Using cv2.imshow() method  
# Displaying the image  
cv2.imshow('window_name', img) 
  
#waits for user to press any key  
#(this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(0)  
  
#closing all open windows  
cv2.destroyAllWindows()  
