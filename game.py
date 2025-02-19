import pygame
import random
import time
from draw import draw_road, draw_start_end_lines

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
player_CAR_WIDTH, player_CAR_HEIGHT = 50, 90
computer_CAR_WIDTH, computer_CAR_HEIGHT = 100, 90
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

# Load Car Images
player_car = pygame.image.load("assets/player_car.png")
player_car = pygame.transform.scale(player_car, (player_CAR_WIDTH, player_CAR_HEIGHT))

enemy_car = pygame.image.load("assets/computer_car.png")
enemy_car = pygame.transform.scale(enemy_car, (computer_CAR_WIDTH, computer_CAR_HEIGHT))

# Game Variables
player_x, player_y = WIDTH // 3 + 80, HEIGHT - 120
enemy_x, enemy_y = 2 * WIDTH // 3 - 80, HEIGHT - 120
player_speed = 5
enemy_speed = 3
race_started = False
winner = None

# Font
font = pygame.font.Font(None, 50)
go_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)
restart_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 140, 50)

# Countdown Before Race
def countdown():
    for i in range(3, 0, -1):
        screen.fill(WHITE)
        draw_road()
        draw_start_end_lines(screen, WIDTH, HEIGHT)
        text = font.render(str(i), True, BLACK)
        screen.blit(text, (WIDTH // 2 - 10, HEIGHT // 2 - 50))
        pygame.display.update()
        time.sleep(1)

# Game Loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    draw_road()
    draw_start_end_lines(screen, WIDTH, HEIGHT)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if go_button.collidepoint(event.pos):
                countdown()
                race_started = True
                winner = None
                player_x, player_y = WIDTH // 4 + 110, HEIGHT - 80
                enemy_x, enemy_y = (3 * WIDTH) // 4 -160, HEIGHT - 80
            if winner and restart_button.collidepoint(event.pos):
                race_started = False
                winner = None
    
    if not race_started:
        pygame.draw.rect(screen, RED, go_button)
        text = font.render("GO", True, WHITE)
        screen.blit(text, (go_button.x + 25, go_button.y + 10))
    else:
        if winner is None:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > WIDTH // 3:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < 2 * WIDTH // 3 - CAR_WIDTH:
                player_x += player_speed
            if keys[pygame.K_UP] and player_y > 0:
                player_y -= player_speed
            if keys[pygame.K_DOWN] and player_y < HEIGHT - CAR_HEIGHT:
                player_y += player_speed
            
            # Enemy Car Movement
            enemy_y -= enemy_speed
            
            # Check for Finish Line
            if player_y <= 50:
                winner = "Player"
            if enemy_y <= 50:
                winner = "Enemy"
        
        # Draw Cars
        screen.blit(player_car, (player_x, player_y))
        screen.blit(enemy_car, (enemy_x, enemy_y))
        
        if winner:
            text = font.render(f"{winner} Wins!", True, BLACK)
            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.draw.rect(screen, BLUE, restart_button)
            restart_text = font.render("Restart", True, WHITE)
            screen.blit(restart_text, (restart_button.x + 10, restart_button.y + 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
