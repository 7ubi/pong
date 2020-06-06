import pygame
import math
import numpy as np
from paddle import Paddle
from ball import *

pygame.init()

width, height = 600, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PONG")
myfont = pygame.font.SysFont('Arial', 60)

clock = pygame.time.Clock()

left = Paddle(95, 200, 10, 75, 5)
right = Paddle(495, 200, 10, 75, 5)


def gameLoop():
	left.y = 200
	right.y = 200

	ball = Ball(width/2, height/2, 10, 4, np.pi)
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
			
		ball.checkBottom(height)
		ball.checkSide(width, gameLoop, left, right)	
		ball.checkLeftPaddle(left)
		ball.checkRightPaddle(right)
		ball.update()
		ball.show(screen)

		text = myfont.render(f"{left.score} : {right.score}", True, (255, 255, 255))
		textRect = text.get_rect()
		textRect.center = (300, 100)
		screen.blit(text, textRect)

		pygame.display.update()
		clock.tick(60)

gameLoop()
