#importing the libraries
import pygame
import random
import datetime

#WINDOWS size
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Global variables
started = False
paddle_1_speed = 0
paddle_2_speed = 0
PADDLE_SPEED = 5
score_1 = 0
score_2 = 0
# play with this to increase or decrease the speed of the ball
BALL_SPEED = 30
game_start_time = 0
time_elapsed = 0
score_animation = None
animation_timer = 0
base_ball_speed = 30

# rectangle representing the paddles
paddle_1_rect = pygame.Rect(30, 0, 7, 100)
paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

# rectangle representing the ball
ball_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 25, 25)

ball_accel_x = random.randint(2,4) * 0.1
ball_accel_y = random.randint(2,4) * 0.1

clock = pygame.time.Clock()

#randomizing the initial direction of the ball
if random.randint(1,2):
    ball_accel_x *= -1
if random.randint(1,2):
    ball_accel_y *= -1

#----------------------------------------------------------#

def reset_ball():
    global ball_accel_x, ball_accel_y
    ball_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_accel_x = random.randint(2,4) * 0.1
    ball_accel_y = random.randint(2,4) * 0.1
    if random.randint(1,2):
        ball_accel_x *= -1
    if random.randint(1,2):
        ball_accel_y *= -1

def check_and_display_winner():
    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)
    if score_1 >= 10:
        return "Player 1 WINS!", COLOR_GREEN
    elif score_2 >= 10:
        return "Player 2 WINS!", COLOR_GREEN
    elif score_1 < -1 or score_2 < -1:
        if score_1 < -1:
            return "Player 2 WINS! (Player 1 is out)", COLOR_RED
        else:
            return "Player 1 WINS! (Player 2 is out)", COLOR_RED
    return None, None

def main():
    global started, paddle_1_speed, paddle_2_speed, ball_accel_x, ball_accel_y, score_1, score_2, game_start_time, time_elapsed, score_animation, animation_timer, base_ball_speed, BALL_SPEED

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PONG GAME")

    score_font = pygame.font.Font(None, 48)
    animation_font = pygame.font.Font(None, 60)
    winner_font = pygame.font.Font(None, 72)
    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)

    while True:
        clock.tick(60)  
        screen.fill(COLOR_BLACK)

        if started and game_start_time == 0:
            game_start_time = pygame.time.get_ticks()
        
        if started:
            time_elapsed = (pygame.time.get_ticks() - game_start_time) / 1000
            BALL_SPEED = base_ball_speed + (time_elapsed * 0.5)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True

        winner_text, winner_color = check_and_display_winner()
        if winner_text:
            winner_display = winner_font.render(winner_text, True, winner_color)
            winner_rect = winner_display.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(winner_display, winner_rect)
            pygame.display.update()
            continue

        keys = pygame.key.get_pressed()
        paddle_1_speed = 0
        paddle_2_speed = 0
        
        if keys[pygame.K_w]:
            paddle_1_speed = -PADDLE_SPEED
        if keys[pygame.K_s]:
            paddle_1_speed = PADDLE_SPEED
            
        if keys[pygame.K_UP]:
            paddle_2_speed = -PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            paddle_2_speed = PADDLE_SPEED

        paddle_1_rect.y += paddle_1_speed
        paddle_2_rect.y += paddle_2_speed

        paddle_1_rect.y = max(0, min(SCREEN_HEIGHT - paddle_1_rect.height, paddle_1_rect.y))
        paddle_2_rect.y = max(0, min(SCREEN_HEIGHT - paddle_2_rect.height, paddle_2_rect.y))
            
        if started:
            ball_rect.x += ball_accel_x * BALL_SPEED
            ball_rect.y += ball_accel_y * BALL_SPEED
            
        if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
            ball_accel_y *= -1

        if ball_rect.colliderect(paddle_1_rect) and ball_accel_x < 0:
            ball_accel_x *= -1
        if ball_rect.colliderect(paddle_2_rect) and ball_accel_x > 0:
            ball_accel_x *= -1

        if ball_rect.left <= 0:
            score_2 += 1
            score_animation = f"+1 (Player 2)"
            animation_timer = 30
            if not (ball_rect.colliderect(paddle_1_rect)):
                score_1 -= 1
            reset_ball()
        elif ball_rect.right >= SCREEN_WIDTH:
            score_1 += 1
            score_animation = f"+1 (Player 1)"
            animation_timer = 30
            if not (ball_rect.colliderect(paddle_2_rect)):
                score_2 -= 1
            reset_ball()

        if not started:
            font = pygame.font.Font(None, 30)
            text = font.render("Press SPACE to start the game", True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        score_text = score_font.render(f"{score_1}   {score_2}", True, COLOR_WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 40))
        screen.blit(score_text, score_rect)

        if score_animation and animation_timer > 0:
            alpha = int((animation_timer / 30) * 255)
            anim_text = animation_font.render(score_animation, True, COLOR_GREEN)
            anim_rect = anim_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(anim_text, anim_rect)
            animation_timer -= 1

        pygame.display.update()




if __name__ == "__main__":
    main()
