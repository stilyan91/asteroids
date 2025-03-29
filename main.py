import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    dt = 0

    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)    
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
    
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        player.update(dt)
            
    
if __name__ == "__main__":
    main()
    