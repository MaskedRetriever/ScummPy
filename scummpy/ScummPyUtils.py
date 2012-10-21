import sys, os, pygame
from pygame.locals import *

def GetIndex(color):
	#Awful hack that is the result of not having 256 colors
	#This pallette is also an awful hack, designed to be at
	#least slightly legible to human eyes because damn.
	#print(color)
	if color == (0,0,0):
		return 0
	if color == (255,0,0):
		return 1
	if color == (0,255,0):
		return 2
	if color == (255,255,0):
		return 3
	if color == (0,0,255):
		return 4
	if color == (255,0,255):
		return 5
	if color == (0,255,255):
		return 6
	if color == (255,255,255):
		return 7
	if color == (127,127,127):
		return 8
	if color == (0,127,127):
		return 9
	if color == (127,0,127):
		return 10
	if color == (127,127,0):
		return 11
	if color == (0,0,127):
		return 12
	if color == (127,0,0):
		return 13
	if color == (0,127,0):
		return 14
	if color == (255,127,127):
		return 15
	if color == (127,255,127):
		return 16
	if color == (127,127,255):
		return 17
	if color == (255,127,0):
		return 18
	if color == (255,0,127):
		return 19
	if color == (0,255,127):
		return 20
	if color == (127,255,0):
		return 21
	if color == (127,0,255):
		return 22
	if color == (0,127,255):
		return 23
	return 0
	
def TexNum(number):
	if number>99:
		return str(number)
	if number>9:
		return "0" + str(number)
	return "00" + str(number)

def CoordMap(iPos, iScale, oScale):
	XScale = (float(oScale[0])/float(iScale[0]))
	YScale = (float(oScale[0])/float(iScale[0]))
	XPos= int(XScale*iPos[0])
	YPos= int(YScale*iPos[1])
	return (XPos,YPos)
