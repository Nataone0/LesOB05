import pygame

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Класс для блоков
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# Класс для ракетки


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def move_left(self):
        self.speed = -10

    def move_right(self):
        self.speed = 10

# Класс для мяча


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = [4, -4]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]

# Создание спрайтов


paddle = Paddle(GREEN, 100, 10)
paddle.rect.x = (WIDTH // 2) - (paddle.rect.width // 2)
paddle.rect.y = HEIGHT - 20

ball = Ball(WHITE, 20, 20)
ball.rect.x = WIDTH // 2
ball.rect.y = HEIGHT // 2

blocks = pygame.sprite.Group()
for i in range(5):  # 5 рядов блоков
    for j in range(12):  # 8 блоков в каждом ряду
        block = Block(RED, 75, 30)
        block.rect.x = 75 * j + 20
        block.rect.y = 30 * i + 20
        blocks.add(block)

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle)
all_sprites.add(ball)
for block in blocks:
    all_sprites.add(block)


# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.move_left()
            elif event.key == pygame.K_RIGHT:
                paddle.move_right()

    all_sprites.update()

    # Проверка столкновений мяча с ракеткой
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed[1] = -ball.speed[1]

    # Проверка столкновений мяча с блоками
    block_hit_list = pygame.sprite.spritecollide(ball, blocks, True)
    for block in block_hit_list:
        ball.speed[1] = -ball.speed[1]

    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
