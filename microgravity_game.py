import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zero-G Sports Arena")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define player properties
player_size = 50
player_x, player_y = screen_width // 2, screen_height // 2
player_velocity = [0, 0]  # Velocity for x and y directions
max_speed = 5

# Game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keypress handling for movement in zero gravity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_velocity[1] -= 0.1  # Move up
    if keys[pygame.K_s]:
        player_velocity[1] += 0.1  # Move down
    if keys[pygame.K_a]:
        player_velocity[0] -= 0.1  # Move left
    if keys[pygame.K_d]:
        player_velocity[0] += 0.1  # Move right

    # Limit player speed
    player_velocity[0] = max(-max_speed, min(max_speed, player_velocity[0]))
    player_velocity[1] = max(-max_speed, min(max_speed, player_velocity[1]))

    # Update player position
    player_x += player_velocity[0]
    player_y += player_velocity[1]

    # Boundary conditions
    if player_x < 0 or player_x > screen_width - player_size:
        player_velocity[0] = -player_velocity[0]  # Bounce back
    if player_y < 0 or player_y > screen_height - player_size:
        player_velocity[1] = -player_velocity[1]  # Bounce back

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
    pygame.display.flip()

    # Frame rate
    clock.tick(60)
