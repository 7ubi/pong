import pygame
from paddle import Paddle

pygame.init()

width, height = 600, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PONG")

clock = pygame.time.Clock()

left = Paddle(95, 200, 10, 75, 3)
right = Paddle(495, 200, 10, 75, 3)


def gameLoop():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return

		key = pygame.key.get_pressed()
		if key[pygame.K_w]:
			left.move(-1)

		if key[pygame.K_s]:
			left.move(1)

		if key[pygame.K_UP]:
			right.move(-1)

		if key[pygame.K_DOWN]:
			right.move(1)


		screen.fill(pygame.Color(0, 0, 0))
		left.show(screen)
		right.show(screen)
		pygame.display.update()
		clock.tick(60)

gameLoop()
