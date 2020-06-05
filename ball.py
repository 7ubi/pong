import pygame

class ball:
	def __init__(self, x, y, w, h, speed, angle, dir):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speed = speed
		self.angle = angle
		self.dir = dir