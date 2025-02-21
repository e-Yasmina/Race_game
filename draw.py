import pygame

# Game Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)

def draw_road(screen, WIDTH, HEIGHT):
    # Draw the road itself
    pygame.draw.rect(screen, GRAY, (WIDTH // 3, 0, WIDTH // 3, HEIGHT))  # Road

    # Left and Right lane markers
    pygame.draw.line(screen, WHITE, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), 5)  # Left lane
    pygame.draw.line(screen, WHITE, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), 5)  # Right lane

    # Dashed middle line
    dash_length = 20  # Length of each dash
    for i in range(0, HEIGHT, dash_length * 2):
        pygame.draw.line(screen, WHITE, (WIDTH // 2, i), (WIDTH // 2, i + dash_length), 3)

    # Draw the side lines (left and right edges)
    pygame.draw.line(screen, WHITE, (WIDTH // 3 - 10, 0), (WIDTH // 3 - 10, HEIGHT), 5)  # Left edge
    pygame.draw.line(screen, WHITE, (2 * WIDTH // 3 + 10, 0), (2 * WIDTH // 3 + 10, HEIGHT), 5)  # Right edge



def draw_start_end_lines(screen, WIDTH, HEIGHT):
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 100, WIDTH, 10))  # Start line
    pygame.draw.rect(screen, GREEN, (0, 50, WIDTH, 10))  # Finish line
