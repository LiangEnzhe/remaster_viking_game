import pygame
from random import randint
import sys
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.mouse.set_visible(False)

# Constants
ASSETS_DIR = 'img'
FPS = 30
WIDTH, HEIGHT = 500, 768
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game settings
speed = 10
speed_limit = 20
scroll = 0

# Setup the screen/display window (this must come before loading any images)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("упал")
clock = pygame.time.Clock()

# Load images once (now it's safe to load them since the display is initialized)
background = pygame.image.load(os.path.join(ASSETS_DIR, "bg.jpeg")).convert()
player_img = pygame.image.load(os.path.join(ASSETS_DIR, "viking1.png")).convert()
pol_img = pygame.image.load(os.path.join(ASSETS_DIR, "pol.png")).convert()
fly_img = pygame.image.load(os.path.join(ASSETS_DIR, "fly.png")).convert()
pivo_img = pygame.image.load(os.path.join(ASSETS_DIR, "pivo.png")).convert()
pakak_img = pygame.image.load(os.path.join(ASSETS_DIR, "3.png")).convert()
comix_img = pygame.image.load(os.path.join(ASSETS_DIR, "beginning.png")).convert()

# Classes
class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, size, pos, colorkey=None):
        super().__init__()
        self.image = pygame.transform.scale(image, size)
        if colorkey:
            self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        pass

class MovingObject(GameObject):
    def __init__(self, image, size, pos, speed, colorkey=None):
        super().__init__(image, size, pos, colorkey)
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class Player(GameObject):
    def __init__(self):
        super().__init__(player_img, (100, 68), (WIDTH / 2, HEIGHT / 3), WHITE)
        self.current_health = 100
        self.max_health = 100
        self.health_bar_length = 450
        self.health_ratio = self.max_health / self.health_bar_length

    def get_damage(self, amount):
        global game_over, speed, speed_limit
        if self.current_health > 0:
            self.current_health -= amount
            if self.current_health <= 0:
                pygame.time.wait(1000)
                self.current_health = 100
                speed = 20
                speed_limit = 20
                game_over = True

    def get_health(self, amount):
        if self.current_health < self.max_health:
            self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def basic_health(self):
        pygame.draw.rect(screen, RED, (10, 10, self.current_health / self.health_ratio, 25))
        pygame.draw.rect(screen, BLACK, (10, 10, self.health_bar_length, 25), 4)

class ObjectSpawner:
    def __init__(self, spawn_class, spawn_rate, *args):
        self.spawn_class = spawn_class
        self.spawn_rate = spawn_rate
        self.args = args
        self.objects = pygame.sprite.Group()

    def spawn(self):
        if randint(0, self.spawn_rate) == 0:
            obj = self.spawn_class(*self.args)
            self.objects.add(obj)
            return obj
        return None

# Game initialization
def beginning():
    comix = pygame.transform.scale(comix_img, (WIDTH, HEIGHT))
    comix_rect = comix.get_rect(topleft=(0, 0))
    screen.blit(comix, comix_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    waiting = False

def show_go_screen():
    screen.fill(WHITE)
    fnt = pygame.font.Font(os.path.join(ASSETS_DIR, "font", "LSANS.TTF"), 45)
    t1 = fnt.render("''JUST FALL''", True, BLACK)
    t3 = fnt.render("Pls click to begin", True, BLACK)
    screen.blit(t1, (WIDTH / 2 - 125, HEIGHT / 2 - 125))
    screen.blit(t3, (WIDTH / 2 - 150, HEIGHT / 2 - 50))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    waiting = False

# Game loop
def game_loop():
    global speed, speed_limit, scroll
    player = Player()
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    fly = pygame.sprite.Group()
    pol = pygame.sprite.Group()
    piv = pygame.sprite.Group()

    # Object spawners with speed argument included
    pakak_spawner = ObjectSpawner(MovingObject, 15, pakak_img, (400, 50), (randint(0, 350), HEIGHT + 400), speed)
    pakak2_spawner = ObjectSpawner(MovingObject, 15, pakak_img, (400, 50), (randint(0, 350) + 150, HEIGHT + 400), speed)
    fly_spawner = ObjectSpawner(MovingObject, 5, fly_img, (50, 50), (randint(1, 9) * 50, HEIGHT - 200), speed)
    pivo_spawner = ObjectSpawner(MovingObject, 5, pivo_img, (50, 50), (randint(1, 9) * 50, HEIGHT - 200), speed)

    game_over = False
    while not game_over:
        # Handle speed limits and game dynamics
        if speed < speed_limit:
            speed += 0.2
        elif speed < 0:
            speed = 0

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update objects
        scroll -= speed
        if scroll <= -800:
            scroll = 0
        screen.blit(background, (0, scroll))
        screen.blit(background, (0, 800 + scroll))

        # Object spawning
        pakak_spawner.spawn()
        pakak2_spawner.spawn()
        fly_spawner.spawn()
        pivo_spawner.spawn()

        all_sprites.update()

        # Collision checks
        if pygame.sprite.spritecollide(player, mobs, True):
            speed = 5
            player.get_damage(20)

        # Draw everything
        all_sprites.draw(screen)
        player.basic_health()
        player.update()
        pygame.display.update()

# Start the game
beginning()
game_loop()
