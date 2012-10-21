#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *
#814x32
class BlitFont:
	
	def __init__(self, FontPath="resources/font_1.png"):
		#self.FontPlate = pygame.transform.scale(pygame.image.load("font_1.png"),(814*2,32*2))
		self.FontPlate = pygame.image.load(FontPath)
		self.XCaps = 8
		self.YCaps = 0
		self.Hs = 10
		self.FontPlate.set_colorkey((255,0,255))
		#self.LetterXCaps=(4, 16, 26, 36,46,55,64, 75, 85, 90, 98, 108, 117, 128, 138, 149, 158, 169, 179,188,198, 207, 219, 231,242,252)
		#self.LetterWCaps=(7,5,5,5,4,4,6,4,1,3,5,4,5,5,6,4,6,5,5,6,4,7,8,6,7,6)
		self.LetterX=(0,2,5,12,18,28,35,37,41,45,49,55,58,62,64,68,74,80,86,92,98,104,110,116,122,128,131,134,140,146,152,158,168,177,184,191,198,204,210,218,225,226,232,239,245,253,260,268,274,282,289,295,302,308,317,326,333,341,349,352,354,358,362,369,373,379,385,391,397,403,407,413,419,420,423,428,430,438,444,450,456,462,466,471,475,481,487,496,503,509,514,519,521,525,531)
		
		
	def BlitText(self, imDest, xyDest, text):
		#demo
		cursor=0;
		
		for C in text:
			cha=ord(C)
			#print(cha)
			if cha == 32:
				cursor=cursor+4
			else:
				charwidth=(self.LetterX[cha-32]-self.LetterX[cha-33])
				imDest.blit(self.FontPlate,(xyDest[0]+cursor,xyDest[1]),Rect(self.LetterX[cha-33],self.YCaps,charwidth,self.Hs))
				cursor=cursor+charwidth+1

	def BlitTextCenter(self, imDest, xyDest, text):
		#demo
		cursor=0;
		imTray=pygame.Surface((320,40))
		imTray.fill((255,0,255))
		imTray.set_colorkey((255,0,255))
		
		for C in text:
			cha=ord(C)
			#print(cha)
			if cha == 32:
				cursor=cursor+4
			else:
				charwidth=(self.LetterX[cha-32]-self.LetterX[cha-33])
				imTray.blit(self.FontPlate,(cursor,0),Rect(self.LetterX[cha-33],self.YCaps,charwidth,self.Hs))
				cursor=cursor+charwidth+1
		imDest.blit(imTray,(xyDest[0]-(cursor/2),xyDest[1]))		
		
#In order, now:
# !"#$%&'()*+,-./0123456789:;<=>?
#@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
#`abcdefghijklmnopqrstuvwxyz{|}~		