# _*_coding:utf-8 _*_
# import modules
from SimpleCV import *

# variables charged
cam = Camera()  # get images from camera
txt = "TARGET: O.K"  # Text to show
img = cam.getImage()  # Get images from camera
width = img.width
height = img.height

# Main loop
while True:
    img = cam.getImage()
    img = img.erode(7)
    new_layer = DrawingLayer(img.size())
    new_layer.selectFont('arialblack')
    new_layer.text(txt, (width/2, height/4), color=Color.CRIMSON)
    img.addDrawingLayer(new_layer)
    img.show()

