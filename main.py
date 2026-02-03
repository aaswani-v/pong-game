#importing the libraries
import pygame
import random

#WINDOWS size
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)


# rectangle representing the paddles
paddle_1_rect = pygame.Rect(30, 0, 7, 100)
paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

paddle_1_speed = 0
paddle_2_speed = 0
PADDLE_SPEED = 0

# rectangle representing the ball
ball_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 25, 25)

ball_accel_x = random.randint(2,4) * 0.1
ball_accel_y = random.randint(2,4) * 0.1

clock = pygame.time.Clock()
started = False

#randomizing the initial direction of the ball
if random.randint(1,2):
    ball_accel_x *= -1
if random.randint(1,2):
    ball_accel_y *= -1

#----------------------------------------------------------#

def main():
    global started  

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PONG GAME")

    while True:
        clock.tick(60)  
        screen.fill(COLOR_BLACK)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True

                if event.key == pygame.K_w:
        paddle_1_speed = -PADDLE_SPEED
    if event.key == pygame.K_s:
        paddle_1_speed = PADDLE_SPEED
    if event.key == pygame.K_UP:
        paddle_2_speed = -PADDLE_SPEED
    if event.key == pygame.K_DOWN:
        paddle_2_speed = PADDLE_SPEED

        if not started:
            font = pygame.font.Font(None, 30)
            text = font.render("Press SPACE to start the game", True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        pygame.display.update()




if __name__ == "__main__":
    main()
