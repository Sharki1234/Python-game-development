import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

images = [pygame.image.load(f"pygame/sk{i+1}.png") for i in range(8)]
index = 0

while True:
    clock.tick(10)
    screen.fill((255,255,255))
    image = images[index]
    screen.blit(image,(250,250))
    index = (index + 1) % len(images)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    clock.tick(60)
    