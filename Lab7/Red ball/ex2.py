import pygame

pygame.init()

x = 30
y = 30

screen = pygame.display.set_mode((1000, 700))

running = False

color = ('Red')

clock = pygame.time.Clock()

while not running:
    
    for event in pygame.event.get():
        # Если пользователь закрывает окно
        if event.type == pygame.QUIT:
            running = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 20
        if y - 25 < 0:
            y = 25
    if pressed[pygame.K_DOWN]:
        y += 20
        if y + 25 > 675:
            y = 675
    if pressed[pygame.K_LEFT]:
        x -= 20
        if x - 25 < 0:
            x = 25
    if pressed[pygame.K_RIGHT]:
        x += 20
        if x + 25 > 1000:
            x = 975
    
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, color, (x, y), 25)
    
    # Обновление экрана
    pygame.display.flip()
    
    clock.tick(60)
# Завершаем работу Pygame
pygame.quit()