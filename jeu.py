import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

import Menus
from Boutons import Button
from Menus import *

pygame.display.set_caption("Ultimate Archer")
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets2", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size):
    path = join("assets2", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "Human", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "right"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


def get_background(name):
    image = pygame.image.load(join("assets2", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image, player1, player2, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player1.draw(window, offset_x)
    player2.draw(window, offset_x)

    pygame.display.update()

'''def draw(window, background, bg_image, player1, player2, objects, offset_x, p2_arrows, p1_arrows, p2_health, p1_health):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player1.draw(window, offset_x)
    player2.draw(window, offset_x)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(p2_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(p1_health), 1, WHITE)
    window.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    window.blit(yellow_health_text, (10, 10))

    for arrow in p2_arrows:
        pygame.draw.rect(window, RED, arrow)

    for arrow in p1_arrows:
        pygame.draw.rect(window, YELLOW, arrow)

    pygame.display.update()'''

'''def draw_window(p2_arrows, p1_arrows, p2_health, p1_health):
    # window.blit(SPACE, (0, 0))
    # pygame.draw.rect(window, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(p2_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(p1_health), 1, WHITE)
    window.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    window.blit(yellow_health_text, (10, 10))

    for arrow in p2_arrows:
        pygame.draw.rect(window, RED, arrow)

    for arrow in p1_arrows:
        pygame.draw.rect(window, YELLOW, arrow)'''



def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if (keys[pygame.K_LEFT] or keys[pygame.K_q]) and not collide_left:
        player.move_left(PLAYER_VEL)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()








BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

#BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
#BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

ARROW_VEL = 7
MAX_ARROWS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

PLAYER1 = pygame.USEREVENT + 1   # YELLOW
PLAYER2 = pygame.USEREVENT + 2   # RED

'''YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))'''


def draw_window(red, yellow, red_bullets, yellow_bullets, p2_health, p1_health):
    # window.blit(SPACE, (0, 0))
    pygame.draw.rect(window, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(p2_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(p1_health), 1, WHITE)
    window.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    window.blit(yellow_health_text, (10, 10))

    # window.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    # window.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(window, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(window, YELLOW, bullet)

    pygame.display.update()


'''def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - PLAYER_VEL > 0:  # LEFT
        yellow.x -= PLAYER_VEL
    if keys_pressed[pygame.K_d] and yellow.x + PLAYER_VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += PLAYER_VEL
    if keys_pressed[pygame.K_w] and yellow.y - PLAYER_VEL > 0:  # UP
        yellow.y -= PLAYER_VEL
    if keys_pressed[pygame.K_s] and yellow.y + PLAYER_VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += PLAYER_VEL'''


'''def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - PLAYER_VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= PLAYER_VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + PLAYER_VEL + red.width < WIDTH:  # RIGHT
        red.x += PLAYER_VEL
    if keys_pressed[pygame.K_UP] and red.y - PLAYER_VEL > 0:  # UP
        red.y -= PLAYER_VEL
    if keys_pressed[pygame.K_DOWN] and red.y + PLAYER_VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += PLAYER_VEL'''


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += ARROW_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER2))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= ARROW_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER1))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    window.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                            2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)
    Menus.main_menu(SCREEN)


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    p2_arrows = []   # ok
    p1_arrows = []   # ok

    p2_health = 10   # ok
    p1_health = 10   # ok

    clock = pygame.time.Clock()   # ok
    run = True   # ok
    while run:   # ok
        clock.tick(FPS)   # ok
        for event in pygame.event.get():   # ok
            if event.type == pygame.QUIT:   # ok
                run = False   # ok
                pygame.quit()   # ok

            if event.type == pygame.KEYDOWN:   # ok
                if event.key == pygame.K_LCTRL and len(p1_arrows) < MAX_ARROWS:   # ok
                    bullet = pygame.Rect(   # ok
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)   # ok
                    p1_arrows.append(bullet)   # ok
                    #BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(p2_arrows) < MAX_ARROWS:   # ok
                    bullet = pygame.Rect(   # ok
                        red.x, red.y + red.height//2 - 2, 10, 5)   # ok
                    p2_arrows.append(bullet)   # ok
                    #BULLET_FIRE_SOUND.play()

            if event.type == PLAYER2:   # ok
                p2_health -= 1   # ok
                #BULLET_HIT_SOUND.play()

            if event.type == PLAYER1:   # ok
                p1_health -= 1   # ok
                #BULLET_HIT_SOUND.play()

        winner_text = ""   # ok
        if p2_health <= 0:   # ok
            winner_text = "Yellow Wins!"   # ok

        if p1_health <= 0:   # ok
            winner_text = "Red Wins!"   # ok

        if winner_text != "":   # ok
            draw_winner(winner_text)   # ok
            break   # ok

        '''keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)'''

        handle_bullets(p1_arrows, p2_arrows, yellow, red)   # ok

        draw_window(red, yellow, p2_arrows, p1_arrows,
                    p2_health, p1_health)

    main()



















def game(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("earth.png")

    block_size = 96

    player1 = Player(100, 100, 50, 50)
    player2 = Player(WIDTH-100, 100, 50, 50)
    fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
    fire.on()
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),
               Block(block_size * 3, HEIGHT - block_size * 4, block_size), fire]

    offset_x = 0
    scroll_area_width = 200

    p2_arrows = []
    p1_arrows = []

    p2_health = 10
    p1_health = 10

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player1.jump_count < 2:
                    player1.jump()

                if event.key == pygame.K_RCTRL and len(p2_arrows) < MAX_ARROWS:
                    arrow = pygame.Rect(
                        player1.rect.x, player1.rect.y + player1.rect.height//2 - 2, 10, 5)
                    p2_arrows.append(arrow)
                    #BULLET_FIRE_SOUND.play()

                '''if event.key == pygame.K_LCTRL and len(p1_arrows) < MAX_ARROWS:
                    arrow = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    p1_arrows.append(arrow)
                    #BULLET_FIRE_SOUND.play()'''

            if event.type == PLAYER2:
                p2_health -= 1
                #BULLET_HIT_SOUND.play()

            if event.type == PLAYER1:
                p1_health -= 1
                #BULLET_HIT_SOUND.play()

        winner_text = ""
        if p2_health <= 0:
            winner_text = "P2 Wins!"

        if p1_health <= 0:
            winner_text = "P1 Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        handle_bullets(p2_arrows, p1_arrows, player2.rect, player1.rect)   # le 2eme player1.rect doit être modifié







        player1.loop(FPS)
        player2.loop(FPS)
        fire.loop()
        handle_move(player1, objects)
        handle_move(player2, objects)
        draw(window, background, bg_image, player1, player2, objects, offset_x)#, p2_arrows, p1_arrows,p2_health, p1_health)


        # draw_window(PLAYER2, PLAYER1, p2_arrows, p1_arrows,
        #             p2_health, p1_health)

        if ((player1.rect.right - offset_x >= WIDTH - scroll_area_width) and player1.x_vel > 0) or (
                (player1.rect.left - offset_x <= scroll_area_width) and player1.x_vel < 0):
            offset_x += player1.x_vel

        if ((player2.rect.right - offset_x >= WIDTH - scroll_area_width) and player2.x_vel > 0) or (
                (player2.rect.left - offset_x <= scroll_area_width) and player2.x_vel < 0):
            offset_x += player2.x_vel

    pygame.quit()
    quit()