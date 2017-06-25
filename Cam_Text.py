# _*_coding:utf-8 _*_

# author: Marco García Baturan
# date: 2017/06/25
# Licence: GNU
# Theme: A.I, C.V

# import modules
from SimpleCV import *
"""
Simple script in python where capture the camera in computer , give some erode to picture and
add some text."""

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

