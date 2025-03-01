import pygame
from random import randint
import sys
import os

# Ensure the img_dir is correctly referenced
img_dir = 'img'

FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 500
HEIGHT = 768

pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)

def beginning():
    comix = pygame.transform.scale(comix_img, (500, 768))
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
    fnt = pygame.font.Font(os.path.join(img_dir, "font", "LSANS.TTF"), 45)
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 68))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(player_img, (100, 68))
        self.image.set_colorkey(WHITE)
        self.rect.center = (WIDTH / 2, HEIGHT / 3)
        self.current_health = 100
        self.max_health = 100
        self.health_bar_length = 450
        self.health_ratio = self.max_health / self.health_bar_length

    def get_damage(self, amount):
        global game_over
        global speed_limit
        global speed
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

    def update(self):
        self.rect.x = x

    def basic_health(self):
        pygame.draw.rect(screen, RED, (10, 10, self.current_health / self.health_ratio, 25))
        pygame.draw.rect(screen, BLACK, (10, 10, self.health_bar_length, 25), 4)

def bg(scroll):
    screen.blit(background, (0, scroll))
    screen.blit(background, (0, 800 + scroll))

class Pakak(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global random_num1
        global speed
        self.image = pygame.Surface((400, 50))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(pakak_img, (400, 50))
        self.rect.topright = (random_num1, HEIGHT + 400 * t)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

class Pakak2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global random_num1
        global speed
        self.image = pygame.Surface((400, 50))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(pakak_img, (400, 50))
        self.rect.topleft = (random_num1 + 150, HEIGHT + 400 * t)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

class Fly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global speed
        global random_num2
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(fly_img, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect.topright = (random_num2 * 50, HEIGHT - 200 + 4000 * s + 400 * random_num2)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

class Pivo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global speed
        global random_num2
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(pivo_img, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect.topright = (random_num3 * 50, HEIGHT - 200 + 4000 * s + 400 * random_num3)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

class Potolok(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global speed
        global random_num1
        self.image = pygame.Surface((150, 50))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(pol_img, (150, 50))
        self.rect.topleft = (random_num1, HEIGHT + 400 * t)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("упал")
clock = pygame.time.Clock()
scroll = 0
speed = 10
speed_limit = 20

background = pygame.image.load(os.path.join(img_dir, "bg.jpeg")).convert()
player_img = pygame.image.load(os.path.join(img_dir, "viking1.png")).convert()
pol_img = pygame.image.load(os.path.join(img_dir, "pol.png")).convert()
fly_img = pygame.image.load(os.path.join(img_dir, "fly.png")).convert()
pivo_img = pygame.image.load(os.path.join(img_dir, "pivo.png")).convert()
pakak_img = pygame.image.load(os.path.join(img_dir, "3.png")).convert()
comix_img = pygame.image.load(os.path.join(img_dir, "beginning.png")).convert()

game_over = True
running = True
beginning()
while running:
    if speed < speed_limit:
        speed += 0.2
    elif speed < 0:
        speed = 0

    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        player = Player()
        fly = pygame.sprite.Group()
        pol = pygame.sprite.Group()
        piv = pygame.sprite.Group()
        all_sprites.add(player)
        for t in range(100):
            random_num1 = randint(0, 350)
            m = Pakak()
            y = Pakak2()
            p = Potolok()
            all_sprites.add(m, y, p)
            pol.add(p)
            mobs.add(m, y)
        for s in range(8):
            random_num2 = randint(1, 9)
            random_num3 = randint(1, 9)
            f = Fly()
            u = Pivo()
            all_sprites.add(f, u)
            piv.add(u)
            fly.add(f)
    x, y = pygame.mouse.get_pos()
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    scroll -= speed
    if scroll <= -800:
        scroll = 0
    bg(scroll)
    all_sprites.update()

    if pygame.sprite.spritecollide(player, mobs, True):
        speed = 5
        player.get_damage(20)

    IDONTKNOWWHATITMEANS = pygame.sprite.spritecollide(player, pol, True)
    if pygame.sprite.spritecollide(player, fly, True):
        speed = -8
        speed_limit -= 2

    if pygame.sprite.spritecollide(player, piv, True):
        player.get_damage(-20)

    all_sprites.draw(screen)
    player.basic_health()
    player.update()
    pygame.display.update()