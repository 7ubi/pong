import pygame
import math
import numpy as np
from paddle import Paddle


def map(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    valueScaled = float(value - leftMin) / float(leftSpan)

    return rightMin + (valueScaled * rightSpan)

class Ball:
	def __init__(self, x, y, r, speed, angle):
		self.x = x
		self.y = y
		self.r = r
		self.speed = speed
		self.angle = angle

	def update(self):
		self.x += math.cos(self.angle) * self.speed
		self.y += math.sin(self.angle) * self.speed

		self.x = int(self.x)
		self.y = int(self.y)

	def changeAngle(self, angle):
		self.angle = angle

	def changeDir(self):
		self.dir *= -1

	def checkBottom(self, height):
		if self.y > height - self.r:
			self.changeAngle(-self.angle)
			self.y = height - self.r
		if self.y < self.r:
			self.changeAngle(-self.angle)
			self.y = self.r

	def checkSide(self, width, func, l, r):
		if self.x < 0:
			r.score += 1
			func()
			
		if self.x > width:
			l.score += 1
			func()

	def checkLeftPaddle(self, p):
		if self.x < p.x + p.w + self.r and self.x > p.x - self.r and self.y > p.y - self.r and self.y < p.y + p.h + self.r:
			self.x = p.x + p.w + self.r
			dy = self.y - p.y
			self.angle = map(dy, 0, p.h, -45 * np.pi / 180, 45 * np.pi / 180)

	def checkRightPaddle(self, p):
		if self.x < p.x + p.w + self.r and self.x > p.x - self.r and self.y > p.y - self.r and self.y < p.y + p.h + self.r:
			self.x = p.x - self.r
			dy = self.y - p.y
			self.angle = map(dy, 0, p.h, 225 * np.pi / 180, 135 * np.pi / 180)

	def show(self, screen):
		pygame.draw.circle(screen, pygame.Color(255, 255, 255), (int(self.x), int(self.y)), self.r)
