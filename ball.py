import pygame
import math


class Ball:
	def __init__(self, x, y, r, speed, angle, dir):
		self.x = x
		self.y = y
		self.r = r
		self.speed = speed
		self.angle = angle
		self.dir = dir

	def update(self):
		self.x += math.cos(self.angle * -self.dir) * self.dir * self.speed
		self.y += math.sin(self.angle * -self.dir) * self.dir * self.speed

		self.x = int(self.x)
		self.y = int(self.y)

	def changeAngle(self, angle):
		self.angle = angle

	def changeDir(self):
		self.dir *= -1

	def show(self, screen):
		pygame.draw.circle(screen, pygame.Color(255, 255, 255), (int(self.x), int(self.y)), self.r)
