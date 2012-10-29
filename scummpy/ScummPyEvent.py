import pygame
from pygame.locals import *
import os

class Command:
	def __init__(self, verb="Walk", noun="box", noun2="nothing"):
		self.verb=verb
		self.noun=noun
		self.noun2=noun2

