import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Инициализация шрифта для отображения счета

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Класс для ракеток
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 70)

    def move(self, y):
        self.rect.y += y
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > height - 70:
            self.rect.y = height - 70


# Класс для мяча
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.vx = random.choice([-4, 4])
        self.vy = random.choice([-4, 4])

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.y <= 0 or self.rect.y >= height - 10:
            self.vy = -self.vy


def draw(paddle, opponent, ball, player_score, opponent_score):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle.rect)
    pygame.draw.rect(screen, WHITE, opponent.rect)
    pygame.draw.ellipse(screen, WHITE, ball.rect)
    score_text = font.render(f"{player_score} : {opponent_score}", True, WHITE)
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 20))
    pygame.display.flip()


def reset_ball(ball):
    ball.rect.x = width // 2
    ball.rect.y = height // 2
    ball.vx = random.choice([-4, 4])
    ball.vy = random.choice([-4, 4])


def game():
    paddle = Paddle(width - 20, height // 2)
    opponent = Paddle(10, height // 2)
    ball = Ball(width // 2, height // 2)

    player_score = 0
    opponent_score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle.move(-5)
        if keys[pygame.K_DOWN]:
            paddle.move(5)

        opponent.move(2 if ball.rect.y > opponent.rect.y else -2)

        if ball.rect.colliderect(paddle.rect) or ball.rect.colliderect(opponent.rect):
            ball.vx = -ball.vx

        ball.move()

        if ball.rect.x <= 0:
            player_score += 1
            reset_ball(ball)
        elif ball.rect.x >= width:
            opponent_score += 1
            reset_ball(ball)

        if player_score == 3 or opponent_score == 3:
            print(f"Игра окончена. Счет {player_score}:{opponent_score}")
            running = False

        draw(paddle, opponent, ball, player_score, opponent_score)
        clock.tick(60)

    return True


# Цикл для повторения игры
while True:
    if not game():
        break
    if input("Хотите сыграть еще раз? (да/нет): ").lower() != "да":
        break
