import pygame

class Paddle:
	def __init__(self, x, y, w, h, speed):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speed = speed

	def move(self, dir, height):
		if self.y >= 0 and self.y + self.h <= height or self.y <= 0 and dir == 1 or self.y + self.h >= height and dir == -1:
			self.y += dir * self.speed
	

	def show(self, screen):
		pygame.draw.rect(screen, pygame.Color(255, 255, 255), (self.x, self.y, self.w, self.h))