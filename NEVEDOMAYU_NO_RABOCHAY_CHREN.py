#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, random, sys
import pygame
from pygame.locals import *
import os

pygame.init()
all_sprites = pygame.sprite.Group()

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

class Score():
    def __init__(self):
        super().__init__()        
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
        self.maxcount = 100    
    def update(self):
        self.counter += 1
        key = pygame.key.get_pressed()

        # Movement
        if key[K_UP]:
            self.rect.centery += -6
        if key[K_DOWN]:
            self.rect.centery += 6
        if key[K_RIGHT]:
            self.rect.centerx += 6
        if key[K_LEFT]:
            self.rect.centerx += -6

        # Restrictions
        self.rect.bottom = min(self.rect.bottom, 730)
        self.rect.top = max(self.rect.top, 50)
        self.rect.right = min(self.rect.right, 1268)
        self.rect.left = max(self.rect.left, 12)        
        if self.counter > self.maxcount:
            self.kill()
class Fire(pygame.sprite.Sprite): # Нужно разобрать

    def __init__(self):
        super().__init__(all_sprites)

        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('data/fire1.png')
        self.image = pygame.transform.scale(self.image, (20, 40))
        self.rect = self.image.convert().get_rect()
        self.x_dist = 5
        self.y_dist = 5
        self.rect.centery = 410
        self.rect.centerx = 640
    def update(self):
        key = pygame.key.get_pressed()

        # Movement
        if key[K_UP]:
            self.rect.centery += -6
        if key[K_DOWN]:
            self.rect.centery += 6
        if key[K_RIGHT]:
            self.rect.centerx += 6
        if key[K_LEFT]:
            self.rect.centerx += -6

        # Restrictions
        self.rect.bottom = min(self.rect.bottom, 750)
        self.rect.top = max(self.rect.top, 70)
        self.rect.right = min(self.rect.right, 1268)
        self.rect.left = max(self.rect.left, 12)

class Player(pygame.sprite.Sprite): # Нужно разобрать

    def __init__(self):
        super().__init__(all_sprites)

        #pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('data/gg3.png', '-1')
        self.image = pygame.transform.scale(self.image, (45, 75))
        self.rect = self.image.convert().get_rect()
        self.x_dist = 2
        self.y_dist = 2
        self.lasertimer = 0
        self.lasermax = 50
        self.rect.centery = 360
        self.rect.centerx = 640
        self.hp = 15
        #self.all_sprites = all_sprites
        self.k = 0
    def update(self):
        key = pygame.key.get_pressed()

        # Movement
        if key[K_UP]:
            self.rect.centery += -6
        if key[K_DOWN]:
            self.rect.centery += 6
        if key[K_RIGHT]:
            self.rect.centerx += 6
        if key[K_LEFT]:
            self.rect.centerx += -6
        # Lasers

        if s.cou < 50:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                x = Laser(self.rect.midtop)
                all_sprites.add(x)
                laserSprites.add(x)
                self.lasertimer = 0
        elif s.cou >= 50 and s.cou < 100:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                x1 = Laser((self.rect.left, self.rect.top + 10))
                y1 = Laser((self.rect.right, self.rect.top + 15))
                all_sprites.add(x1)
                all_sprites.add(y1)
                laserSprites.add(x1)
                laserSprites.add(y1)
                self.lasertimer = 0
        elif s.cou >= 100:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                x2 = Laser(self.rect.midtop)
                y2 = Laser((self.rect.left, self.rect.top + 10))
                z2 = Laser((self.rect.right, self.rect.top + 15))
                all_sprites.add(x2)                    
                all_sprites.add(y2)
                all_sprites.add(z2)  
                laserSprites.add(x2)
                laserSprites.add(y2)
                laserSprites.add(z2)                
                self.lasertimer = 0                

        # Restrictions
        self.rect.bottom = min(self.rect.bottom, 720)
        self.rect.top = max(self.rect.top, 0)
        self.rect.right = min(self.rect.right, 1280)
        self.rect.left = max(self.rect.left, 0)
        
        if pygame.sprite.groupcollide(playerSprite, laserSprites_e, 0, 1):
            all_sprites.add(PlayerExplosion(player.rect.center))
            self.hp -= 1
            hpl.update()
        if pygame.sprite.groupcollide(playerSprite, BossLasp, 0, 1):
            all_sprites.add(PlayerExplosion(player.rect.center))
            self.hp -= 1
            hpl.update()
      
        if self.lasermax - 5 > 0 and s.cou % 20 == 0 and s.cou != 0 and s.cou != self.k:
            self.lasermax -= 5
            self.k = s.cou
            self.lasertimer = 0
            all_sprites.add(LelUP(self.rect.center))
  
class hphki():
    def __init__(self):
        super().__init__()
        
        self.fontObj = pygame.font.Font('freesansbold.ttf', 50)    
        self.hp = 15
        self.points = self.fontObj.render('Health Points:' + str(self.hp), 1, (255, 255, 255))
        self.rect = self.points.get_rect()
        self.rect.center = (850, 10)
    def update(self):
        self.hp -= 1
        self.points = self.fontObj.render('Health Points:' + str(self.hp), 1, (255, 255, 255))

hpl = hphki()  

        
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        pygame.sprite.Sprite.__init__(self)
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
        super().__init__(all_sprites)
        

        self.image = pygame.image.load("data/alien.png")
        self.image = pygame.transform.scale(self.image, (30, 60))        
        self.rect = self.image.convert().get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.pok = centerx
        self.dx = 2
        self.dy = 2
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
            all_sprites.remove(self) 
            
            all_sprites.add(AnimatedSprite(self.rect.center))

            s.update()

        # Ship Collisions
        if pygame.sprite.spritecollideany(self, playerSprite ):
            all_sprites.add(AnimatedSprite(self.rect.center))
            all_sprites.add(PlayerExplosion(player.rect.center))
 
            s.update()
            player.hp -= 1
            hpl.update()
            self.kill()
    def reset(self):
        self.rect.bottom = 0
        #self.rect.centerx = random.randrange(0, 600)
        #self.dy = random.randrange(5, 10)
        #self.dx = random.randrange(-2, 2)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, centerx):
        super().__init__()
        
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
            print(2)
            enemy2Sprites.remove(self)
            all_sprites.add(AnimatedSprite(self.rect.center))
            s.update()


        # Ship Collisions
        if pygame.sprite.spritecollideany(self, playerSprite ):
            all_sprites.add(AnimatedSprite(self.rect.center))
            all_sprites.add(PlayerExplosion(player.rect.center))
            s.update()
            hpl.update()
            player.hp -= 1
            self.kill()
            
class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        
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
        super().__init__()
        
        #pygame.sprite.Sprite.__init__(self)
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
            x4 = BossLaser((self.rect.midtop[0], self.rect.midtop[1]+20))
            y4 = BossLaser1((self.rect.left, self.rect.top/2))
            z4 = BossLaser2((self.rect.right, self.rect.top/2))
            all_sprites.add(x4)
            all_sprites.add(y4)
            all_sprites.add(z4)
            BossLasp.add(x4)
            BossLasp.add(y4)
            BossLasp.add(z4)
            self.lasertimer = 0        
    
        # Laser Collisions    
        if pygame.sprite.groupcollide(BossSprite, laserSprites, 0, 1):
            all_sprites.add(AnimatedSprite(self.rect.center))
            s.update()
            self.live()

        # Ship Collisions
        if pygame.sprite.spritecollideany(self, playerSprite ):
            all_sprites.add(AnimatedSprite(self.rect.center))
            all_sprites.add(PlayerExplosion(player.rect.center))
            s.update()
            player.hp -= 1
            hpl.update()
            self.live()
        if self.hp <= 0 and self.f2 == False:
            self.kon = self.p + 80
            self.f2 = True
            all_sprites.add(BossBlust((640, 100)))
            all_sprites.add(BossBlust((400, 50)))
            all_sprites.add(BossBlust((800, 50)))
            all_sprites.add(BossBlust((100, 20)))
            all_sprites.add(BossBlust((1000, 20)))
        if self.p == self.kon and self.f2:
            BossSprite.remove(self)
            self.f2 = False
    def live(self):
        self.hp -= 1
class BossLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        
        #pygame.sprite.Sprite.__init__(self)
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
        super().__init__(all_sprites)
        
        #pygame.sprite.Sprite.__init__(self)    
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
        super().__init__(all_sprites)
        
        #pygame.sprite.Sprite.__init__(self)    
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
pygame.display.set_caption("The Best Game In The World")
FPS = 240


bkgd = pygame.image.load("Data/f.png").convert()
x = 0
y = 0
# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

player = Player()
fire = Fire()

global playerSprite   
playerSprite = pygame.sprite.RenderPlain((player))

global laserSprites
laserSprites = pygame.sprite.RenderPlain(())
global laserSprites_e
laserSprites_e = pygame.sprite.RenderPlain(())
global BossSprite
BossSprite = pygame.sprite.RenderPlain(())

global enemy2Sprites
enemy2Sprites = pygame.sprite.RenderPlain(())




global BossLasp
BossLasp = pygame.sprite.RenderPlain(())

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

    if cu == 7200:
        fb = False
        b = Boss()
        
        BossSprite.add(b)

    elif cu > 2400 and cu % 120 == 0 and fb:
        y1 = Enemy2(random.randrange(0, 1280))
        enemy2Sprites.add(y1)

    elif cu % 60 == 0 and fb:
        x = Enemy(random.randrange(0, 1280), 0)
        all_sprites.add(x)
    if cu > 7200:
        if b.hp <= 0 and b.f2 == False:
            print(4)
            f = False
    BossSprite.update()
    enemy2Sprites.update()
    
    all_sprites.update()
    all_sprites.draw(screen)
    
    BossSprite.draw(screen)
    enemy2Sprites.draw(screen)
    
    screen.blit(hpl.points, hpl.rect.center)
    screen.blit(s.score, s.rect.center)

    
    pygame.display.update()
    pygame.display.flip()    
    CLOCK.tick(FPS)
    
    if player.hp <= 0:
        sco = s.cou
        f = False
        op = 1
    rel_y = y % bkgd.get_rect().height 
    DS.blit(bkgd, (0, rel_y - bkgd.get_rect().height) )
    if rel_y < H:
        DS.blit(bkgd, (0, rel_y))
pygame.init()

def lastscreen():
    screen2 = pygame.display.set_mode((1280, 720))
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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()
        CLOCK.tick(FPS)
def winscreen():
    screen2 = pygame.display.set_mode((1280, 720))
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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        pygame.display.flip()
        CLOCK.tick(FPS)

if op == 1:
    lastscreen()
elif op == 2:
    winscreen()    