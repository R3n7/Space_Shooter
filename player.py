import pygame
from pygame.locals import *
import os
pygame.font.init()
pygame.mixer.init()
class Player():
    def __init__(self, x, y, width, height,color,id):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.bullet = False
        self.id=id
        self.bulletsfired =[ ]
        self.health = 10
        self.hit = False

    def draw(self,win,image):
        #pygame.draw.rect(win, self.color, self.rect)
        win.blit(image,self.rect)
    def move(self):
        #bullet_hit_sound = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
        bullet_fire_sound = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))#sound plays when bullet is fired
        keys = pygame.key.get_pressed()
        self.bullet = False
        if keys[pygame.K_LCTRL]:
            self.bullet = True
            if self.id ==1 and len(self.bulletsfired)==0:
                bullet_fire_sound.play()#sound plays
                self.bulletsfired.append(pygame.Rect(self.x+self.width,self.y+self.height//2-2,10,5))#a rectangle gets appended with the starting pos
            elif self.id ==2 and len(self.bulletsfired)==0:
                bullet_fire_sound.play()
                self.bulletsfired.append(pygame.Rect(self.x,self.y+self.height//2-2,10,5))
        if keys[pygame.K_LEFT]:
            if self.x -self.vel>0:
                self.x -= self.vel#to move left
        if keys[pygame.K_RIGHT]:
            if self.x+self.vel<900-self.width:
                self.x += self.vel#to move right

        if keys[pygame.K_UP]:
            if self.y-self.vel>0:
                self.y -= self.vel#to move up

        if keys[pygame.K_DOWN]:
            if self.y+self.vel<500-self.height:
                self.y += self.vel#to move down

        self.update()
    """
    this function handles the drawing the bullets 
    and checking for collisions with other ship. 
    """
    def firebullet(self,Rect):
        for bullet in self.bulletsfired:
            if self.id == 1:
                bullet.x += 5
                if pygame.Rect.colliderect(Rect,bullet):#checks for collision
                    self.hit =True
                    self.bulletsfired.remove(bullet)#if it is hit then the bullet gets removed from the list
                elif bullet.x>900 :
                    self.bulletsfired.remove(bullet)#if the bullet passes out of the windows,it gets removed
            else:
                bullet.x -= 5
                if pygame.Rect.colliderect(Rect,bullet):
                    self.hit =True
                    self.bulletsfired.remove(bullet)
                elif bullet.x<0:
                    self.bulletsfired.remove(bullet)




    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
