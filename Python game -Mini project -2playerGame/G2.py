import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 10
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)  # Define BLUE color

# Snake class
class Snake:
    def __init__(self, color, initial_pos):
        self.color = color
        self.body = [initial_pos]
        self.direction = "RIGHT"

    def move(self):
        head = self.body[0].copy()
        if self.direction == "RIGHT":
            head[0] += BLOCK_SIZE
        elif self.direction == "LEFT":
            head[0] -= BLOCK_SIZE
        elif self.direction == "UP":
            head[1] -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head[1] += BLOCK_SIZE

        # Adjust head position if out of bounds
        head[0] = max(min(head[0], SCREEN_WIDTH - BLOCK_SIZE), 0)
        head[1] = max(min(head[1], SCREEN_HEIGHT - BLOCK_SIZE), 0)
        
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

# Food class
class Food:
    def __init__(self):
        self.position = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                         random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
        self.color = RED

    def spawn_food(self):
        self.position = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                         random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]

# Function to draw snake
def draw_snake(snake):
    for block in snake.body:
        pygame.draw.rect(screen, snake.color, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Function to check for collision with wall or itself
def check_collision(snake):
    if snake.body[0][0] < 0 or snake.body[0][0] >= SCREEN_WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= SCREEN_HEIGHT:
        return True
    for block in snake.body[1:]:
        if snake.body[0] == block:
            return True
    return False

# Function to check if snake has eaten food
def check_eat_food(snake, food):
    if snake.body[0] == food.position:
        snake.grow()
        food.spawn_food()
        return True
    return False

# Function to display scores
def display_scores(score1, score2):
    font = pygame.font.Font(None, 36)
    score_text1 = font.render(f"Player 1 Score: {score1}", True, WHITE)
    score_text2 = font.render(f"Player 2 Score: {score2}", True, WHITE)
    screen.blit(score_text1, (10, 10))
    screen.blit(score_text2, (10, 40))

# Function to display winner
def display_winner(winner):
    font = pygame.font.Font(None, 50)
    winner_text = font.render(f"The winner is {winner}!", True, WHITE)
    screen.blit(winner_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

# Main function
def main():
    snake1 = Snake(GREEN, [100, 50])
    snake2 = Snake(BLUE, [400, 300])
    food = Food()
    score1 = 0
    score2 = 0
    clock = pygame.time.Clock()
    running = True
    game_over = False
    game_end_time = None

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake1.direction != "DOWN":
                    snake1.direction = "UP"
                elif event.key == pygame.K_DOWN and snake1.direction != "UP":
                    snake1.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake1.direction != "RIGHT":
                    snake1.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake1.direction != "LEFT":
                    snake1.direction = "RIGHT"
                if event.key == pygame.K_w and snake2.direction != "DOWN":
                    snake2.direction = "UP"
                elif event.key == pygame.K_s and snake2.direction != "UP":
                    snake2.direction = "DOWN"
                elif event.key == pygame.K_a and snake2.direction != "RIGHT":
                    snake2.direction = "LEFT"
                elif event.key == pygame.K_d and snake2.direction != "LEFT":
                    snake2.direction = "RIGHT"

        if not game_over:
            snake1.move()
            snake2.move()
            if check_collision(snake1) or check_collision(snake2):
                game_over = True
                game_end_time = time.time()
            if check_eat_food(snake1, food):
                score1 += 1
            if check_eat_food(snake2, food):
                score2 += 1

            draw_snake(snake1)
            draw_snake(snake2)
            pygame.draw.rect(screen, food.color, pygame.Rect(food.position[0], food.position[1], BLOCK_SIZE, BLOCK_SIZE))
            display_scores(score1, score2)

        if game_over:
            if time.time() - game_end_time < 5:
                winner = "Player 1" if score1 > score2 else "Player 2" if score2 > score1 else "No one"
                display_winner(winner)
            else:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
