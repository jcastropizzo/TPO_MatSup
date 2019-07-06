from UI import constants as cfg 
import pygame

def start():
    print('HOLA')
    pygame.init()
    SCREEN = pygame.display.set_mode((cfg.get("WIDTH"),cfg.get("HEIGHT") ))
    pygame.display.set_caption(cfg.get("WINDOWNAME"))

    SCREEN.fill(cfg.get("BLACK"))
    pygame.display.flip()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        pygame.draw.rect(SCREEN, cfg.get("GREEN"),(200,450,100,50))
        pygame.display.update()

    pygame.quit()
    