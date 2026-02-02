#importing the libraries
import pygame
import random

#WINDOWS size
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main():
    #GAME SETUP

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PONG GAME")

    while True:
        screen.fill(COLOR_BLACK) #FILL THE SCREEN WITH BLACK COLOR

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()

