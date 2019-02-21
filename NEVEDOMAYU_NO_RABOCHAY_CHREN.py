#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, random, sys
import pygame
from pygame.locals import *
import os

pygame.init()
all_sprites = pygame.sprite.Group()

def terminate():
    pygame.quit()

# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

class Score():
    def __init__(self):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 50)    
        self.cou =  0
        self.score = self.fontObj.render('Score:' + str(self.cou), 1, (255, 255, 255))
        self.rect = self.score.get_rect()
        self.rect.center = (10, 10)
    def update(self):
        self.cou += 1
        self.score = self.fontObj.render('Score:' + str(self.cou), 1, (255, 255, 255))

s = Score()        
        
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(pygame.image.load("data/e.png"), 4, 4)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect.center = pos
        self.counter = 0
        self.maxcount = 10
    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
        sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]        
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()        
        
class BossBlust(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(pygame.image.load("data/bb.png"), 6, 6)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect.center = pos
        self.counter = 0
        self.maxcount = 100
    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
        sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]        
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()        


class LelUP(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.image.load("data/level_up1.png")
        self.image = pygame.transform.scale(self.image, (100, 50))        
        self.rect = self.image.convert().get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = -60 + pos[1]
        self.counter = 0
        self.maxcount = 10    
    def update(self):
        self.counter += 1
        if self.counter > self.maxcount:
            self.kill()
class Fire(pygame.sprite.Sprite): # Нужно разобрать

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('data/fire1.png')
        self.image = pygame.transform.scale(self.image, (20, 40))
        self.rect = self.image.convert().get_rect()
        self.x_dist = 5
        self.y_dist = 5
        self.rect.centery = 392
        self.rect.centerx = 640
    def update(self):
        key = pygame.key.get_pressed()

        # Movement
        if key[K_UP]:
            self.rect.centery += -3
        if key[K_DOWN]:
            self.rect.centery += 3
        if key[K_RIGHT]:
            self.rect.centerx += 3
        if key[K_LEFT]:
            self.rect.centerx += -3

        # Restrictions
        self.rect.bottom = min(self.rect.bottom, 730)
        self.rect.top = max(self.rect.top, 50)
        self.rect.right = min(self.rect.right, 1268)
        self.rect.left = max(self.rect.left, 12)

class Player(pygame.sprite.Sprite): # Нужно разобрать

    def __init__(self, all_sprites):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('data/gg2.png', '-1')
        self.image = pygame.transform.scale(self.image, (45, 75))
        self.rect = self.image.convert().get_rect()
        self.x_dist = 2
        self.y_dist = 2
        self.lasertimer = 0
        self.lasermax = 50
        self.rect.centery = 360
        self.rect.centerx = 640
        self.hp = 10
        self.all_sprites = all_sprites
        self.k = 0
    def update(self):
        key = pygame.key.get_pressed()

        # Movement
        if key[K_UP]:
            self.rect.centery += -3
        if key[K_DOWN]:
            self.rect.centery += 3
        if key[K_RIGHT]:
            self.rect.centerx += 3
        if key[K_LEFT]:
            self.rect.centerx += -3
        # Lasers

        if s.cou < 50:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                laserSprites.add(Laser(self.rect.midtop))
                self.lasertimer = 0
        elif s.cou >= 50 and s.cou < 100:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                laserSprites.add(Laser((self.rect.left, self.rect.top + 10)))
                laserSprites.add(Laser((self.rect.right, self.rect.top + 15)))
                self.lasertimer = 0
        elif s.cou >= 100:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                laserSprites.add(Laser(self.rect.midtop))                    
                laserSprites.add(Laser((self.rect.left, self.rect.top + 10)))
                laserSprites.add(Laser((self.rect.right, self.rect.top + 15)))                
                self.lasertimer = 0                

        # Restrictions
        self.rect.bottom = min(self.rect.bottom, 720)
        self.rect.top = max(self.rect.top, 0)
        self.rect.right = min(self.rect.right, 1280)
        self.rect.left = max(self.rect.left, 0)
        
        if pygame.sprite.groupcollide(playerSprite, laserSprites_e, 0, 1):
            explosionSprites.add(PlayerExplosion(player.rect.center))
            self.hp -= 1
        if self.lasermax - 5 > 0 and s.cou % 20 == 0 and s.cou != 0 and s.cou != self.k:
            self.lasermax -= 5
            self.k = s.cou
            self.lasertimer = 0
            LelUPSprites.add(LelUP(self.rect.center))
  


           
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/laser1.png")
        self.image = pygame.transform.scale(self.image, (10, 30))        
        self.rect = self.image.convert().get_rect()
        self.rect.center = pos

    def update(self):
        if self.rect.top > 720:
            self.kill()
        else:
            self.rect.move_ip(0, -5)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/alien.png")
        self.image = pygame.transform.scale(self.image, (30, 60))        
        self.rect = self.image.convert().get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.pok = centerx
        self.dx = 1
        self.dy = 1
        self.cou = 0
        self.max1 = 10
    def update(self):
         
        self.rect.centery += self.dy
        if self.rect.top > 720:
            self.reset()
        if self.rect.top > 350:
            if self.rect.centerx == 0:
                self.pok = 100
            elif self.rect.centerx >= 1280:
                self.pok = 650
            if self.pok >= 640:
                self.rect.centerx -= self.dx
            elif self.pok < 640:
                self.rect.centerx += self.dx
        # Laser Collisions
        if pygame.sprite.spritecollideany(self, laserSprites):
            explosionSprites.add(AnimatedSprite(self.rect.center))
            s.update()
            self.kill()

        # Ship Collisions
        if pygame.sprite.spritecollideany(self, playerSprite ):
            explosionSprites.add(AnimatedSprite(self.rect.center))
            explosionSprites.add(PlayerExplosion(player.rect.center))
            s.update()
            player.hp -= 1
            self.kill()
    def reset(self):
        self.rect.bottom = 0
        #self.rect.centerx = random.randrange(0, 600)
        #self.dy = random.randrange(5, 10)
        #self.dx = random.randrange(-2, 2)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/alien2.png")
        self.image = pygame.transform.scale(self.image, (30, 60))        
        self.rect = self.image.convert().get_rect()
        self.rect.centerx = centerx
        self.pok = centerx
        self.dx = 1
        self.lasertimer = 0
        self.lasermax = 100        
    def update(self):
        self.lasertimer += 1
        if self.rect.centerx <= 0:
            self.pok = 100
        elif self.rect.centerx >= 1280:
            self.pok = 650
        if self.pok >= 640:
            self.rect.centerx -= self.dx
        elif self.pok < 640:
            self.rect.centerx += self.dx
        if self.lasertimer == self.lasermax:
            laserSprites_e.add(EnemyLaser(self.rect.midtop))
            self.lasertimer = 0        
            
        # Laser Collisions    
        if pygame.sprite.spritecollideany(self, laserSprites):
            explosionSprites.add(AnimatedSprite(self.rect.center))
            s.update()
            self.kill()

        # Ship Collisions
        if pygame.sprite.spritecollideany(self, playerSprite ):
            explosionSprites.add(AnimatedSprite(self.rect.center))
            explosionSprites.add(PlayerExplosion(player.rect.center))
            s.update()
            player.hp -= 1
            self.kill()
            
class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/e_laser.png")
        self.image = pygame.transform.scale(self.image, (10, 30))        
        self.rect = self.image.convert().get_rect()
        self.rect.center = pos

    def update(self):
        if self.rect.top > 720:
            self.kill()
        else:
            self.rect.move_ip(0, 5)
            
class PlayerExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
            super().__init__(all_sprites)
            self.frames = []
            #self.dragon = (pygame.image.load("e.png"), [4, 4], pos)
            self.cut_sheet(pygame.image.load("data/e.png"), 4, 4)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            self.rect.center = pos
            self.counter = 0
            self.maxcount = 10
 
    def cut_sheet(self, sheet, columns, rows):
            self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
            sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
    def update(self):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]        
            self.counter = self.counter + 1
            if self.counter == self.maxcount:

                self.kill()
                self.counter = 0
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/boss.png")
        self.image = pygame.transform.scale(self.image, (1280, 300))        
        self.rect = self.image.convert().get_rect()
        self.rect.centerx = 640
        self.dx = 1
        self.lasertimer = 0
        self.lasermax = 12
        self.mask = pygame.mask.from_surface(self.image)
        self.hp = 100
        self.p = 0
        self.f2 = False
        self.kon = -1
    def update(self):
        self.p += 1
        self.lasertimer += 1

        if self.lasertimer == self.lasermax:
            laserSprites_e.add(BossLaser((self.rect.midtop[0], self.rect.midtop[1]+20)))
            laserSprites_e.add(BossLaser1((self.rect.left, self.rect.top/2)))
            laserSprites_e.add(BossLaser2((self.rect.right, self.rect.top/2)))            
            self.lasertimer = 0        
    
        # Laser Collisions    
        if pygame.sprite.groupcollide(BossSprite, laserSprites, 0, 1):
            explosionSprites.add(AnimatedSprite(self.rect.center))
            s.update()
            self.live()

        # Ship Collisions
        if pygame.sprite.spritecollideany(self, playerSprite ):
            explosionSprites.add(AnimatedSprite(self.rect.center))
            explosionSprites.add(PlayerExplosion(player.rect.center))
            s.update()
            player.hp -= 1
            self.live()
        if self.hp <= 0 and self.f2 == False:
            self.kon = self.p + 80
            self.f2 = True
            BossBlustsprite.add(BossBlust((640, 100)))
            BossBlustsprite.add(BossBlust((400, 50)))
            BossBlustsprite.add(BossBlust((800, 50)))
            BossBlustsprite.add(BossBlust((100, 20)))
            BossBlustsprite.add(BossBlust((1000, 20)))
        if self.p == self.kon and self.f2:
            self.kill()
            self.f2 = False
    def live(self):
        self.hp -= 1
class BossLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/b_l.png")
        self.image = pygame.transform.scale(self.image, (10, 30))        
        self.rect = self.image.convert().get_rect()
        self.rect.center = pos
        self.na = random.randrange(-5, 5)
    def update(self):
        if self.rect.top > 720:
            self.kill()
        else:
            self.rect.move_ip(self.na, 5)
class BossLaser1(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)    
        self.image = pygame.image.load("data/b_l.png")
        self.image = pygame.transform.scale(self.image, (10, 30))        
        self.rect = self.image.convert().get_rect()
        self.rect.center = pos
        self.na = random.randrange(0, 5)
    def update(self):
        if self.rect.top > 720:
            self.kill()
        else:
            self.rect.move_ip(self.na, 5)
class BossLaser2(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)    
        self.image = pygame.image.load("data/b_l.png")
        self.image = pygame.transform.scale(self.image, (10, 30))        
        self.rect = self.image.convert().get_rect()
        self.rect.center = pos
        self.na = random.randrange(-5, 0)
    def update(self):
        if self.rect.top > 720:
            self.kill()
        else:
            self.rect.move_ip(self.na, 5)
# define display surface			
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

os.environ['CDL_VIDEO_WINDOW_POS'] = "50,50"

# initialise display
screen = pygame.display.set_mode((1280, 720))

CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet -Seamless Background Scrolling")
FPS = 240


bkgd = pygame.image.load("Data/f.png").convert()
x = 0
y = 0
# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

player = Player(all_sprites)
fire = Fire()
global explosionSprites
explosionSprites = pygame.sprite.RenderPlain(())
global playerSprite   
playerSprite = pygame.sprite.RenderPlain((player))
FireSprites = pygame.sprite.RenderPlain((fire))
global laserSprites
laserSprites = pygame.sprite.RenderPlain(())
global laserSprites_e
laserSprites_e = pygame.sprite.RenderPlain(())
global BossSprite
BossSprite = pygame.sprite.RenderPlain(())

global BossBlustsprite
BossBlustsprite = pygame.sprite.RenderPlain(())

global LelUPSprites
LelUPSprites = pygame.sprite.RenderPlain(())

global enemySprites
enemySprites = pygame.sprite.RenderPlain(())
global enemy2Sprites
enemy2Sprites = pygame.sprite.RenderPlain(())

global enemyExplosion
enemyExplosion = pygame.sprite.RenderPlain(())

global playerExplosion
playerExplosion = pygame.sprite.RenderPlain(())
cou = 0
# main loop
def start_screen():
    intro_text = ["Space Battle"]

    fon = pygame.transform.scale(pygame.image.load('data/space_battle.png'), (1280, 720))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('BLACK'))
        intro_rect = string_rendered.get_rect()
        text_coord += 100
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        CLOCK.tick(FPS)

start_screen()


f = True
fb = True
cu = 0
op = 2
while f:
    events()
    
    rel_y = y % bkgd.get_rect().height
    DS.blit(bkgd, (0, rel_y - bkgd.get_rect().height) )
    if rel_y < H:
        DS.blit(bkgd, (0, rel_y))
    y += 1
    cu += 1

    if cu == 14400:
        fb = False
        b = Boss()
        BossSprite.add(b)

    elif cu > 2400 and cu % 120 == 0 and fb:
        enemy2Sprites.add(Enemy2(random.randrange(0, 1280)))   
    elif cu % 60 == 0 and fb:
        enemySprites.add(Enemy(random.randrange(0, 1280), 0))
    if cu > 14400:
        if b.hp <= 0 and b.f2 == False:
            f = False
    fire.update()
    laserSprites.update()
    laserSprites_e.update()    
    enemySprites.update()
    enemy2Sprites.update()
    LelUPSprites.update()
    BossSprite.update() 
    BossBlustsprite.update()
    enemyExplosion.update()
    explosionSprites.update()
    playerExplosion.update()
    player.update()
    BossSprite.draw(screen)
    playerSprite.draw(screen)
    BossBlustsprite.draw(screen)
    FireSprites.draw(screen)
    laserSprites.draw(screen)
    laserSprites_e.draw(screen)    
    enemySprites.draw(screen)
    LelUPSprites.draw(screen)
    enemy2Sprites.draw(screen)
    screen.blit(s.score, s.rect.center)
    enemyExplosion.draw(screen)
    explosionSprites.draw(screen)
    playerExplosion.draw(screen)
    
    #pygame.draw.line(DS, (0, 0, 0), (0, rel_y), (H*2, rel_y), 3)
    pygame.display.update()
    pygame.display.flip()    
    #CLOCK.tick(FPS)
    
    if player.hp <= 0:
        sco = s.cou
        f = False
        op = 1
pygame.init()
screen2 = pygame.display.set_mode((1280, 720))
def lastscreen():
    intro_text = ["You have killed " + str(s.cou) + " alien capitalists! Well played!!!"]

    fon = pygame.transform.scale(pygame.image.load('data/ls.png'), (1280, 720))
    screen2.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 0
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('WHITE'))
        intro_rect = string_rendered.get_rect()
        text_coord += 310
        intro_rect.top = text_coord
        intro_rect.x = 200
        text_coord += intro_rect.x
        screen2.blit(string_rendered, intro_rect)
        
def winscreen():
    intro_text = ["ВЫ прошли эту игру!)"]

    fon = pygame.transform.scale(pygame.image.load('data/win.png'), (1280, 720))
    screen2.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 0
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('White'))
        intro_rect = string_rendered.get_rect()
        text_coord += 300
        intro_rect.top = text_coord
        intro_rect.x = 540
        text_coord += intro_rect.x
        screen2.blit(string_rendered, intro_rect)
if op == 1:
    lastscreen()
elif op == 2:
    winscreen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.flip()
    