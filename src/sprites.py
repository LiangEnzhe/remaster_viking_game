import pygame, os
from src import config

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

image_directory = os.path.join(os.path.dirname(__file__), "assets")

background_image = pygame.image.load(os.path.join(image_directory, "background.png")).convert()
player_image_asset = pygame.image.load(os.path.join(image_directory, "original_viking.png")).convert()
hurt_player_image_asset = pygame.image.load(os.path.join(image_directory, "hurt_viking.png")).convert()
ceiling_obstacle_image_asset = pygame.image.load(os.path.join(image_directory, "break.png")).convert_alpha()
enemy_fly_image_asset = pygame.image.load(os.path.join(image_directory, "wing.png")).convert_alpha()
health_beer_image_asset = pygame.image.load(os.path.join(image_directory, "beer.png")).convert_alpha()
platform_image_asset = pygame.image.load(os.path.join(image_directory, "floor.png")).convert_alpha()
intro_image_asset = pygame.image.load(os.path.join(image_directory, "beginning.png")).convert()
death_cutscene_asset = pygame.image.load(os.path.join(image_directory, "death.png")).convert()

pygame.mixer.music.load(os.path.join(image_directory, "background.mp3"))
pygame.mixer.music.play(-1)
scream_sound = pygame.mixer.Sound(os.path.join(image_directory, "scream.mp3"))
steve_sound = pygame.mixer.Sound(os.path.join(image_directory, "steve.mp3"))
drink_sound = pygame.mixer.Sound(os.path.join(image_directory, "drink.mp3"))
wing_sound = pygame.mixer.Sound(os.path.join(image_directory, "wing.mp3"))