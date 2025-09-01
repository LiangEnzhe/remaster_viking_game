from pygame import *
from random import *
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

init()
mixer.init()
mouse.set_visible(False)

def beginning():
    comix = transform.scale(comix_img, (500, 768))
    comix_rect = comix.get_rect(topleft=(0, 0))
    screen.blit(comix, comix_rect)
    display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for i in event.get():
            if i.type == QUIT:
                quit()
            if i.type == MOUSEBUTTONDOWN:
                if i.button == 1:
                    waiting = False

def show_go_screen():
    screen.fill(WHITE)
    fnt = font.Font(os.path.join(img_dir, "font", "LSANS.TTF"), 45)
    t1 = fnt.render("''JUST FALL''", True, BLACK)
    t3 = fnt.render("Pls click to begin", True, BLACK)
    screen.blit(t1, (WIDTH / 2 - 125, HEIGHT / 2 - 125))
    screen.blit(t3, (WIDTH / 2 - 150, HEIGHT / 2 - 50))
    display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for i in event.get():
            if i.type == QUIT:
                quit()
            if i.type == MOUSEBUTTONDOWN:
                if i.button == 1:
                    waiting = False

class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((100, 68))
        self.rect = self.image.get_rect()
        self.image = transform.scale(player_img, (100, 68))
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
                time.wait(1000)
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
        draw.rect(screen, (255, 0, 0), (10, 10, self.current_health / self.health_ratio, 25))
        draw.rect(screen, (0, 0, 0), (10, 10, self.health_bar_length, 25), 4)

def bg(scroll):
    screen.blit(background, (0, scroll))
    screen.blit(background, (0, 800 + scroll))

class Pakak(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        global random_num1
        global speed
        self.image = Surface((400, 50))
        self.rect = self.image.get_rect()
        self.image = transform.scale(pakak_img, (400, 50))
        self.rect.topright = (random_num1, HEIGHT + 400 * t)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

class Pakak2(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        global random_num1
        global speed
        self.image = Surface((400, 50))
        self.rect = self.image.get_rect()
        self.image = transform.scale(pakak_img, (400, 50))
        self.rect.topleft = (random_num1 + 150, HEIGHT + 400 * t)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

class Fly(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        global speed
        global random_num2
        self.image = Surface((40, 40))
        self.rect = self.image.get_rect()
        self.image = transform.scale(fly_img, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect.topright = (random_num2 * 50, HEIGHT - 200 + 4000 * s + 400 * random_num2)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

class Pivo(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        global speed
        global random_num2
        self.image = Surface((40, 40))
        self.rect = self.image.get_rect()
        self.image = transform.scale(pivo_img, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect.topright = (random_num3 * 50, HEIGHT - 200 + 4000 * s + 400 * random_num3)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

class Potolok(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        global speed
        global random_num1
        self.image = Surface((150, 50))
        self.rect = self.image.get_rect()
        self.image = transform.scale(pol_img, (150, 50))
        self.rect.topleft = (random_num1, HEIGHT + 400 * t)
    def update(self):
        self.rect.y -= speed
        if self.rect.y == 0:
            self.kill()

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("упал")
clock = time.Clock()
scroll = 0
speed = 10
speed_limit = 20

background = image.load(os.path.join(img_dir, "bg.jpeg")).convert()
player_img = image.load(os.path.join(img_dir, "viking1.png")).convert()
pol_img = image.load(os.path.join(img_dir, "pol.png")).convert()
fly_img = image.load(os.path.join(img_dir, "fly.png")).convert()
pivo_img = image.load(os.path.join(img_dir, "pivo.png")).convert()
pakak_img = image.load(os.path.join(img_dir, "3.png")).convert()
comix_img = image.load(os.path.join(img_dir, "beginning.png")).convert()

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
        all_sprites = sprite.Group()
        mobs = sprite.Group()
        player = Player()
        fly = sprite.Group()
        pol = sprite.Group()
        piv = sprite.Group()
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
    x, y = mouse.get_pos()
    clock.tick(FPS)
    for i in event.get():
        if i.type == QUIT:
            running = False
            sys.exit()
            quit()

    scroll -= speed
    if scroll <= -800:
        scroll = 0
    bg(scroll)
    all_sprites.update()

    Ayyyy = sprite.spritecollide(player, mobs, True)
    if Ayyyy:
        speed = 5
        player.get_damage(20)

    Ayyy = sprite.spritecollide(player, pol, True)
    Ayy = sprite.spritecollide(player, fly, True)
    if Ayy:
        speed = -8
        speed_limit -= 2

    Ay = sprite.spritecollide(player, piv, True)
    if Ay:
        player.get_damage(-20)

    all_sprites.draw(screen)
    player.basic_health()
    player.update()
    display.update()

    display.flip()
