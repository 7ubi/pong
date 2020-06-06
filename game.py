import pygame
import math
import numpy as np
from paddle import Paddle
from ball import Ball

pygame.init()

width, height = 600, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PONG")

clock = pygame.time.Clock()



def gameLoop():
	left = Paddle(95, 200, 10, 75, 5)
	right = Paddle(495, 200, 10, 75, 5)

	ball = Ball(width/2, height/2, 10, 4, 0, 1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return

		key = pygame.key.get_pressed()
		if key[pygame.K_w]:
			left.move(-1, height)

		if key[pygame.K_s]:
			left.move(1, height)

		if key[pygame.K_UP]:
			right.move(-1, height)

		if key[pygame.K_DOWN]:
			right.move(1, height)


		screen.fill(pygame.Color(0, 0, 0))

		left.show(screen)
		right.show(screen)

		if ball.x < left.x + left.w + ball.r and ball.x > left.x - ball.r and ball.dir == -1  or ball.x > right.x - ball.r and ball.x < right.x + right.w + ball.r and ball.dir == 1:
			if ball.y > left.y and ball.y <= left.y + left.h / 8 or ball.y > right.y and ball.y <= right.y + right.h / 8:
				ball.changeDir()
				ball.changeAngle(np.pi/4)

			if ball.y > left.y + left.h / 8 and ball.y <= left.y + left.h / 8 * 2 or ball.y > right.y + right.h/8 and ball.y <= right.y + right.h / 8 * 2:
				ball.changeDir()
				ball.changeAngle(30 * np.pi/180)

			if ball.y > left.y + left.h / 8 * 2 and ball.y <= left.y + left.h / 8 * 3 or ball.y > right.y + right.h/8 * 2 and ball.y <= right.y + right.h / 8 * 3:
				ball.changeDir()
				ball.changeAngle(15 * np.pi/180)

			if ball.y > left.y + left.h / 8 * 3 and ball.y <= left.y + left.h / 8 * 5 or ball.y > right.y + right.h/8 * 3 and ball.y <= right.y + right.h / 8 * 5:
				ball.changeDir()
				ball.changeAngle(0)

			if ball.y > left.y + left.h / 8 * 5 and ball.y <= left.y + left.h / 8 * 6 or ball.y > right.y + right.h/8 * 5 and ball.y <= right.y + right.h / 8 * 6:
				ball.changeDir()
				ball.changeAngle(-15 * np.pi/180)

			if ball.y > left.y + left.h / 8 * 6 and ball.y <= left.y + left.h / 8 * 7 or ball.y > right.y + right.h/8 * 6 and ball.y <= right.y + right.h / 8 * 7:
				ball.changeDir()
				ball.changeAngle(-30 * np.pi/180)

			if ball.y > left.y + left.h / 8 * 7 and ball.y <= left.y + left.h or ball.y > right.y + right.h / 8 * 7 and ball.y <= right.y + right.h:
				ball.changeDir()
				ball.changeAngle(-np.pi/4)

			
		if ball.y > height - ball.r or ball.y < ball.r:
			ball.changeAngle(-ball.angle)
			
		if ball.x < 0 or ball.x > width:
			gameLoop()
			return	

		ball.update()
		ball.show(screen)
		pygame.display.update()
		clock.tick(60)

gameLoop()
