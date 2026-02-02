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
            
            pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
            pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

            pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

            pygame.display.update()

paddle_1_rect = pygame.Rect(30, 0, 7, 100)
paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

# tracking the paddle movement
paddle_1_move = 0
paddle_2_move = 0

# rectangle representing the ball
ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

ball_accel_x = random.randint(2,4) * 0.1
ball_accel_y = random.randint(2,4) * 0.1

#randomizing the initial direction of the ball
if random.randint(1,2) * 1:
    ball_accel_x *= -1
if random.randint(1,2) * 1:
    ball_accel_y *= -1



if __name__ == "__main__":
    main()

