import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball!")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 30)

# Ball settings
ball_radius = 30
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_color = RED
ball_speed = 5

# Score
score = 0

# Game loop
def main():
    global ball_x, ball_y, score, ball_speed
    running = True

    while running:
        screen.fill(WHITE)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = ((mouse_x - ball_x) ** 2 + (mouse_y - ball_y) ** 2) ** 0.5

                if distance <= ball_radius:
                    score += 1
                    ball_x = random.randint(ball_radius, WIDTH - ball_radius)
                    ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
                    ball_speed += 1  # Increase speed for challenge

        # Move the ball randomly
        ball_x += random.choice([-ball_speed, ball_speed])
        ball_y += random.choice([-ball_speed, ball_speed])

        # Keep the ball within bounds
        if ball_x < ball_radius:
            ball_x = ball_radius
        elif ball_x > WIDTH - ball_radius:
            ball_x = WIDTH - ball_radius

        if ball_y < ball_radius:
            ball_y = ball_radius
        elif ball_y > HEIGHT - ball_radius:
            ball_y = HEIGHT - ball_radius

        # Draw the ball
        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

        # Display score
        score_text = font.render(f"Score: {score}", True, BLUE)
        screen.blit(score_text, (10, 10))

        # Update display and tick
        pygame.display.flip()
        clock.tick(30)


# Run the game
if __name__ == "__main__":
    main()
