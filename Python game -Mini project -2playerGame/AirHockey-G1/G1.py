import pygame
import random
from paddle import Paddle
from ball import Ball

pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)

size = (700, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Air Hockey")

# Player paddle
paddleA = Paddle(CYAN, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

# AI paddle
paddleB = Paddle(MAGENTA, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# Ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# This will be a list that will contain all the sprites we intend to use
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True
clock = pygame.time.Clock()
scoreA = 0
scoreB = 0

# Winning condition
WINNING_SCORE = 5  # First player to score 5 points wins

# AI Class
class AI:
    def __init__(self, paddle, ball):
        self.paddle = paddle
        self.ball = ball

    def update(self):
        # Simple AI logic
        if self.ball.rect.centery < self.paddle.rect.centery:
            self.paddle.moveUp(10)
        elif self.ball.rect.centery > self.paddle.rect.centery:
            self.paddle.moveDown(10)

# Create AI object
ai = AI(paddleB, ball)

while carryOn:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    # --- Moving the player paddle when the user uses the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(10)
    if keys[pygame.K_s]:
        paddleA.moveDown(10)

    # Update AI
    ai.update()

    # --- Game logic should go here
    all_sprites_list.update()

    # --- Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity = [random.randint(4, 8), random.randint(-8, 8)]
        ball.rect.x = 345
        ball.rect.y = 195

    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity = [random.randint(4, 8), random.randint(-8, 8)]
        ball.rect.x = 345
        ball.rect.y = 195

    if ball.rect.y > 490 or ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    # --- Check for winner
    if scoreA >= WINNING_SCORE or scoreB >= WINNING_SCORE:
        carryOn = False

    # --- Drawing code should go here
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.draw.line(screen, WHITE, [0, 500], [700, 500], 5)
    pygame.draw.rect(screen, WHITE, [345, 0, 10, 600])  # Center line
    pygame.draw.circle(screen, WHITE, [350, 300], 50, 5)  # Center circle

    all_sprites_list.draw(screen)

    # Display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second.
    clock.tick(60)

# Display winner
if scoreA >= WINNING_SCORE:
    winner_text = "Player A wins!"
elif scoreB >= WINNING_SCORE:
    winner_text = "Player B wins!"
else:
    winner_text = "No winner!"

font = pygame.font.Font(None, 100)
text = font.render(winner_text, 1, WHITE)
text_rect = text.get_rect(center=(size[0] // 2, size[1] // 2))
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.delay(3000)

pygame.quit()
