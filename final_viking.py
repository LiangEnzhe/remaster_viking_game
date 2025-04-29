import pygame, sys, random
from random import randint
from src import config
from src import sprites
from src import game_states

pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)

pygame.display.set_caption("")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.transform.scale(sprites.player_image_asset, (120, 140))
        self.hurt_image = pygame.transform.scale(sprites.hurt_player_image_asset, (120, 140))
        self.image = self.original_image
        self.image.set_colorkey(config.BLACK)
        self.rect = self.image.get_rect(center=(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/3))

        self.current_health = 100
        self.target_health = 100
        self.max_health = 100
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 2

        self.hit_timer = 0
        self.is_invulnerable = False

    def get_damage(self, amount):
        global game_over
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health <= 0:
            pygame.time.wait(1000)
            self.target_health = 100
            config.current_scroll_speed = 10
            config.max_scroll_speed = 20
            game_over = True

    def get_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def advanced_health(self):
        transition_width = 0
        transition_color = config.RED

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = config.GREEN

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed 
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255, 255, 0)

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(10, 45, health_bar_width, 25)
        transition_bar = pygame.Rect(health_bar.right, 45, transition_width, 25)
        
        pygame.draw.rect(sprites.screen, config.RED, health_bar)
        pygame.draw.rect(sprites.screen, transition_color, transition_bar)	
        pygame.draw.rect(sprites.screen, config.BLACK, (10, 45, self.health_bar_length, 25), 4)	
          
    def update(self):
        self.rect.x = x
        #self.rect.y = y
        if self.hit_timer > 0:
            self.hit_timer -= 1
            if self.hit_timer <= 0:
                self.image = self.original_image
                self.is_invulnerable = False 

    def change_sprite(self, new_sprite, duration=0):
        self.image = new_sprite
        self.image.set_colorkey(config.BLACK)
        if duration > 0:
            self.hit_timer = duration

class Floor(pygame.sprite.Sprite):
    def __init__(self, side, x_positon_for_floor):
        super().__init__()
        self.image = pygame.Surface((400, 75))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.smoothscale(sprites.platform_image_asset, (400, 75))
        if side == "right":
            self.rect.topleft = (x_positon_for_floor + 170, config.SCREEN_HEIGHT + 400 * number_of_floors)
        elif side == "left":
            self.rect.topright = (x_positon_for_floor, config.SCREEN_HEIGHT + 400 * number_of_floors)
        elif side == "break":
            self.image = pygame.Surface((180, 75))
            self.rect = self.image.get_rect()
            self.image = pygame.transform.scale(sprites.ceiling_obstacle_image_asset, (180, 75))
            self.rect.topleft = (x_positon_for_floor - 5, config.SCREEN_HEIGHT + 400 * number_of_floors)

    def update(self):
        self.rect.y -= config.current_scroll_speed
        if self.rect.y == 0:
            self.kill()

class Collectables(pygame.sprite.Sprite):
    def __init__(self, item):
        super().__init__()
        x_of_horizontal_column = randint(1, 9)
        self.image = pygame.Surface((60, 60))
        self.rect = self.image.get_rect()
        if item == "wing":
            self.image = pygame.transform.smoothscale(sprites.enemy_fly_image_asset, (70, 70))
        elif item == "beer":
            self.image = pygame.transform.smoothscale(sprites.health_beer_image_asset, (70, 70))
        distance_between_items = 3000 
        self.rect.topright = (x_of_horizontal_column * 50, config.SCREEN_HEIGHT - 200 + distance_between_items * amount_of_collectables + 400 * x_of_horizontal_column)

    def update(self):
        self.rect.y -= config.current_scroll_speed
        if self.rect.y == 0:
            self.kill()

def background():
    sprites.screen.blit(sprites.background_image, (0, config.background_scroll))
    sprites.screen.blit(sprites.background_image, (0, 800 + config.background_scroll))

game_over = True
death = 0
game_states.introduction_cutscene()

while True:
    if config.current_scroll_speed < config.max_scroll_speed:
        config.current_scroll_speed += 0.1 #0.1
    elif config.current_scroll_speed < 0:
        config.current_scroll_speed = 0

    if game_over:
        if death != 0:
            game_states.death()
        death = 1
        game_over = False
        config.background_scroll = 0
        All_Sprites_Group = pygame.sprite.Group()
        Non_Breakable_Floor_Group = pygame.sprite.Group()
        player = Player()
        Wing_Group = pygame.sprite.Group()
        Breakable_Floor_Group = pygame.sprite.Group()
        Beer_Group = pygame.sprite.Group()
        All_Sprites_Group.add(player)
        for number_of_floors in range(100):
            x_positon_for_floor = randint(0, 350)
            Left = Floor("left", x_positon_for_floor)
            Right = Floor("right", x_positon_for_floor)
            Breakable = Floor("break", x_positon_for_floor)
            All_Sprites_Group.add(Left, Right, Breakable)
            Breakable_Floor_Group.add(Breakable)
            Non_Breakable_Floor_Group.add(Left, Right)
        for amount_of_collectables in range(20):
            Wings_Object = Collectables("wing")
            Beer_Object = Collectables("beer")
            All_Sprites_Group.add(Wings_Object, Beer_Object)
            Beer_Group.add(Beer_Object)
            Wing_Group.add(Wings_Object)
    
    x, y = pygame.mouse.get_pos()
    clock.tick(config.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    config.background_scroll -= config.current_scroll_speed
    if config.background_scroll <= -config.SCREEN_HEIGHT + 10:
        config.background_scroll = 0

    if pygame.sprite.spritecollide(player, Non_Breakable_Floor_Group, True):
        config.current_scroll_speed = 5
        random.choice([sprites.steve_sound, sprites.scream_sound]).play()
        if not player.is_invulnerable:
            player.change_sprite(player.hurt_image, duration=30) 
            player.is_invulnerable = True
        player.get_damage(20)

    Breakable_Floor = pygame.sprite.spritecollide(player, Breakable_Floor_Group, True)
    
    if pygame.sprite.spritecollide(player, Wing_Group, True):
        config.current_scroll_speed = 0
        sprites.wing_sound.play()

    if pygame.sprite.spritecollide(player, Beer_Group, True):
        player.get_health(20)
        sprites.drink_sound.play()

    background()
    All_Sprites_Group.update()  
    All_Sprites_Group.draw(sprites.screen)
    player.advanced_health()
    player.update()
    pygame.display.update()