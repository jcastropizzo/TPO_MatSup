import constants
import pygame

def start():
    print('HOLA')
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(WINDOWNAME)

    SCREEN.fill(BLACK)
    pygame.display.flip()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

    pygame.quit()
    