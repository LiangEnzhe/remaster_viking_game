import pygame, sys, os
from src import config
from src import sprites

def continue_game_state():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 
            
def introduction_cutscene():
    intro_cutscene = pygame.transform.scale(sprites.intro_image_asset, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    intro_cutscene_rect = intro_cutscene.get_rect() 
    sprites.screen.blit(intro_cutscene, intro_cutscene_rect)
    pygame.display.flip()
    continue_game_state()

def death(): 
    death_cutscene = pygame.transform.scale(sprites.death_cutscene_asset, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    death_cutscene_rect = death_cutscene.get_rect() 
    sprites.screen.blit(death_cutscene, death_cutscene_rect)
    pygame.display.flip()
    continue_game_state()
