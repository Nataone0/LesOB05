import pygame
import time
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test project")

image1 = pygame.image.load("dogz_sprite.com.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("target.com.png")
image_rect2 = image2.get_rect()

speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect1.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect1.x += speed
    if keys[pygame.K_UP]:
        image_rect1.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect1.y += speed
    if event.type == pygame.MOUSEMOTION:
        mouseX, mouseY = pygame.mouse.get_pos()
        image_rect1.x = mouseX - 300
        image_rect1.y = mouseY - 300

    if image_rect1.colliderect(image_rect2):
        print("Collision!")
        time.sleep(1)
    
    screen.fill((0, 0, 50))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.quit()
