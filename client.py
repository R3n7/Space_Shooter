import pygame
from network import Network
from player import Player
import os
pygame.font.init()
pygame.mixer.init()
pygame.init()
#Declaring fonts
health_font = pygame.font.SysFont('Assets/planet5.ttf',30)
winner_font = pygame.font.SysFont('Assets/planet5.ttf',100)
top_font = pygame.font.Font('Assets/planet5.ttf',35)
#declaring Width,heights for the window
width = 900
height = 500
#declaring spaceship width,heights
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40
#creating a background for the window
space = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space1.png')),(width,height))
#creating spaceship images for both players and transforming them to thier respective sizes
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP =  pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
win = pygame.display.set_mode((width, height))#for creating a windoe
pygame.display.set_caption("Client")#title of the window
#loading sounds and playing agame music
bullet_fire_sound = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))
bullet_hit_sound = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
music = pygame.mixer.music.load ("Assets/blassic.ogg") #lost.ogg
pygame.mixer.music.play(-1)

"""
redrawwindow function draws the background,renders fonts,
draws the spaceship and updates,draws health status,bullets. 
"""

def redrawWindow(win,player, player2):
    win.blit(space,(0,0))
    top = top_font.render("SPACE SHOOTER",1,(0,255,0))
    win.blit(top,(225,0))
    #win.fill((255,255,255))
    if player.id ==1:
        player.draw(win,YELLOW_SPACESHIP)
    else:
        player.draw(win,RED_SPACESHIP)
    if player2.id ==1:
        player2.draw(win,YELLOW_SPACESHIP)
    else:
        player2.draw(win,RED_SPACESHIP)
    if player.id ==1:
        p1 = health_font.render("Health:"+str(player.health),1,(0,255,0))
    else:
        p2 =health_font.render("Health:"+str(player.health),1,(0,255,0))
    if player2.id == 1:
        p1 = health_font.render("Health:"+str(player2.health),1,(0,255,0))
    else:
        p2 = health_font.render("Health:"+str(player2.health),1,(0,255,0))
    #yellow_health_text = health_font.render("Health:"+str(player2.health),1,(0,0,0))
    win.blit(p2,(width - p2.get_width()-10,10))
    win.blit(p1,(10,10))

    for bullet in player.bulletsfired:
        if player.id ==1:
            pygame.draw.rect(win,(255,255,0),bullet)
        else:
            pygame.draw.rect(win,(255,0,0),bullet)
    for bullet in player2.bulletsfired:
        if player2.id ==1:
            pygame.draw.rect(win,(255,255,0),bullet)
        else:
            pygame.draw.rect(win,(255,0,0),bullet)
    pygame.display.update()
"""
this fuction is to draw the
winner screen.
"""
def draw_winner(text):
    draw_text = winner_font.render(text,1,(0,255,0))
    win.blit(draw_text,(width//2- draw_text.get_width()//2,height//2-draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    run = True
    n = Network()
    p = n.getP()#receiving the intial pos
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)#sending and receiving objects

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()#quits from pygame window
        p.move()
        p.firebullet(pygame.Rect(p2.rect))
        if p.hit:
            bullet_hit_sound.play()
            p2.health-=1
            p.hit =False
            pygame.time.delay(2)
        p2.firebullet(pygame.Rect(p.rect))
        if p2.hit:
            bullet_hit_sound.play()
            p.health-=1
            p2.hit =False
            pygame.time.delay(2)
        """
        defining the winning condition 
        in the below lines.
        """
        winn = ""
        if p2.health<=0:
            winn ="YOU WIN!"
        elif p.health<=0:
            winn = "YOU LOSE!"
        if len(winn)!=0:
                draw_winner(winn)
                win.fill(pygame.Color("black"))
                winn = "GAME OVER"
                draw_winner(winn)
                break
        redrawWindow(win, p, p2)

main()