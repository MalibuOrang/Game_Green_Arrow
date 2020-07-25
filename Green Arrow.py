import pygame
from pygame.locals import *
import time
import os
import random
from random import randint
from os import path
import math
pygame.init()
win = pygame.display.set_mode((1360,780))
pygame.display.set_caption("Green Arrow")
jump = pygame.mixer.Sound('jump.wav')
go = pygame.mixer.Sound('go_beton.wav')
push_m = pygame.mixer.Sound('push.wav')
pusher = pygame.mixer.Sound('push_h.wav')
sead = pygame.mixer.Sound('sead.wav')
shoot_bow_1 = pygame.mixer.Sound('shoot.wav')
shoot_bow_2 = pygame.mixer.Sound('shoot_bow.wav')
enemy_death = pygame.mixer.Sound('death_enemy.wav')
death_gg = pygame.mixer.Sound('dead_gg.wav')
take = pygame.mixer.Sound('take_med.wav')
use_medcit = pygame.mixer.Sound('use_med.wav')
pygame.mixer.music.load('fon.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png')
,pygame.image.load('R5.png'),pygame.image.load('R6.png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png')
,pygame.image.load('L5.png'),pygame.image.load('L6.png')]
playerStand_R = pygame.image.load('gg_R.png')
playerStand_L = pygame.image.load('gg_L.png')
Shoot_arrow_R = [pygame.image.load('Shoot_s1_R.png'),pygame.image.load('Shoot_s2_R.png'),pygame.image.load('Shoot_s3_R.png'),pygame.image.load('Shoot_s4_R.png'),pygame.image.load('Shoot_s5_R.png')]
Shoot_arrow_L = [pygame.image.load('Shoot_s1_L.png'),pygame.image.load('Shoot_s2_L.png'),pygame.image.load('Shoot_s3_L.png'),pygame.image.load('Shoot_s4_L.png'),pygame.image.load('Shoot_s5_L.png')]
Shoot_arrow_p_R = [pygame.image.load('Shoot_p1_R.png'),pygame.image.load('Shoot_p2_R.png'),pygame.image.load('Shoot_p3_R.png'),pygame.image.load('Shoot_p4_R.png'),pygame.image.load('Shoot_p5_R.png')]
Shoot_arrow_p_L = [pygame.image.load('Shoot_p1_L.png'),pygame.image.load('Shoot_p2_L.png'),pygame.image.load('Shoot_p3_L.png'),pygame.image.load('Shoot_p4_L.png'),pygame.image.load('Shoot_p5_L.png')]
bg = pygame.image.load('bg2.jpg')
jump_r = [pygame.image.load('jump_R.png')]
jump_l = [pygame.image.load('jump_L.png')]
pushr = [pygame.image.load('push_leg_R1.png'),pygame.image.load('push_leg_R2.png')]
pushl = [pygame.image.load('push_leg_L2.png'),pygame.image.load('push_leg_L1.png')]
sead_l = [pygame.image.load('Sead_L.png')]
sead_r = [pygame.image.load('Sead_R.png')]
push_hand_R = [pygame.image.load('Push1.png'),pygame.image.load('Push3.png')]
push_hand_L = [pygame.image.load('Push_L_1.png'),pygame.image.load('Push_L_3.png')]
bul_r = pygame.image.load('bullet.png')
bul_l = pygame.image.load('bullet2.png')
icon_gg_R = pygame.image.load('icon_gg_R.png')
icon_gg_L = pygame.image.load('icon_gg_L.png')
start_menu = pygame.image.load('Start_menu.png')
font = pygame.font.SysFont('serif', 26)
clock = pygame.time.Clock()
x = 10
y = 650
width = 90
height = 106
speed = 10
isJump = False
push = False
jumpCount = 10
left = False
right = False
gg_sead = False
stand_R = False
stand_L = False
push_h = False
sead_sound = True
shoot_arrow = False
shoot_arrow_p = False
shoot_arrow_p_2 = False
death_cound = False
medcit_use = True 
animCount = 0
pushCount = 0
seadCount = 0
handCount = 0
shootCount = 0
shootCount_p = 0
shootCount_p_2 = 0
deathCount = 0
score = 0
hitbox_arrow =(x,y, 71,25)
hitbox_gg =(x,y,90,106)
hitbox_zek = (x+20,y, 90,106)
gg_health = 100
health = 10
def hit_gg():
    global gg_health
    if gg_health > 0:
        gg_health -= 1
        enemy_death.play()
    else:
        go.stop()
        jump.stop()
        sead.stop()
        push_m.stop()
        pusher.stop()
        shoot_bow_1.stop()
        shoot_bow_2.stop()
        menu = pygame.image.load('menu_death.png')
        enemy_death.stop()
        win.blit(menu,(0,0))
        pygame.display.update()
        death_gg.play()
        time.sleep(4)
        pygame.quit()
        quit()

class snaryad():
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 30 * facing
        self.hitbox_arrow =(self.x,self.y, 71,25)
    def draw(self,win):
        if not(stand_R):
            win.blit(bul_l,(self.x,self.y))
        else:
            win.blit(bul_r,(self.x,self.y))
        self.hitbox_arrow = (self.x, self.y, 71,25)
        
def scrollX(win, x):
    width, height = win.get_size()
    copySurf = win.copy()
    win.blit(copySurf, (x, 0))
    if x < 0:
        win.blit(copySurf, (width + x, 0), (0, 0, -x, height))
    else:
        win.blit(copySurf, (0, 0), (width - x, 0, x, height))
class medic(object):
    medcit = pygame.image.load('hp.png')
    def __init__(self, x, y, width, height):
        x_hp = randint(0,1000)
        self.x = x_hp
        self.y = y
        self.width = 70
        self.height = 60
        self.hitbox_med = (self.x, self.y, 70,60)
        self.visible = True
    def draw(self, win):
        if self.visible:
            win.blit(self.medcit, (self.x,self.y))
            self.hitbox_med = (self.x, self.y, 90,106)
            
class enemy(object):
    walkRight = [pygame.image.load('i1.png'), pygame.image.load('i2.png'), pygame.image.load('i3.png'), pygame.image.load('i4.png'), pygame.image.load('i5.png'), pygame.image.load('i6.png'), pygame.image.load('i7.png'), pygame.image.load('i8.png'),pygame.image.load('i9.png'),pygame.image.load('i10.png')]
    walkLeft = [pygame.image.load('i1_L.png'), pygame.image.load('i2_L.png'), pygame.image.load('i3_L.png'), pygame.image.load('i4_L.png'), pygame.image.load('i5_L.png'), pygame.image.load('i6_L.png'), pygame.image.load('i7_L.png'), pygame.image.load('i8_L.png'),pygame.image.load('i9_L.png'),pygame.image.load('i10_L.png')]
    def __init__(self, x, y, width, height, end,health):
        x_zek = randint(0,800)
        end_point = randint(1000,1300)
        self.x = x_zek
        self.y = y
        self.end = end_point
        self.health = health
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.yronCount = 0
        self.vel = 3
        if score > 500:
            self.vel += 3
        self.hitbox_zek = (self.x, self.y, 90,106)
        self.visible = True
    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 30:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            pygame.draw.rect(win,(255,0,0),(self.hitbox_zek[0], self.hitbox_zek[1] -10, 50, 10))
            pygame.draw.rect(win,(0,128,0),(self.hitbox_zek[0], self.hitbox_zek[1] -10, 50-(5  *(10-self.health)), 10))
            self.hitbox_zek = (self.x+20, self.y, 90,106)
            
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def hit(self):
        if self.health > 0:
            self.health -= 1
            enemy_death.play()
        else:
            enemy_death.stop()
            self.visible = False
    def hit_push(self):
        if self.health > 0:
            self.health -= 0.1
            enemy_death.play()
        else:
            enemy_death.stop()
            self.visible = False
            
def menu():
    win.blit(start_menu,(0,0))
    pygame.display.update()


def drawWindow():
    global animCount
    global pushCount
    global seadCount
    global handCount
    global shootCount
    global shootCount_p
    global shootCount_p_2
    global font
    global gg_health
    win.blit(bg,(0,0))
    zek.draw(win)
    hp.draw(win)
    hp_2.draw(win)
    text = font.render('Очки: ' + str(score), 1, (250,15,42))
    win.blit(text, (1200, 10))
    text_hp = font.render('HP: ' + str(gg_health), 1, (250,10,42))
    win.blit(text_hp, (30, 100))
    round(count_medcit)
    text_medcit = font.render('Ресурс аптечек: ' + str(count_medcit), 1, (250,10,42))
    win.blit(text_medcit, (30, 140))
    if animCount + 1 >=30:
        animCount = 0
    if seadCount + 1 >=30:
        seadCount = 0
    if pushCount + 1 >=30:
        pushCount = 0
    if handCount + 1 >=30:
        handCount = 0
    if shootCount + 1 >= 30:
        shootCount = 0
    if shootCount_p + 1 >= 30:
        shootCount_p = 0
    if shootCount_p_2 + 1 >= 30:
        shootCount_p_2 = 0
    if stand_R:
        win.blit(icon_gg_R, (30,10))
    else:
        win.blit(icon_gg_L, (30,10))
    if left:
        win.blit(walkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x,y))
        animCount += 1
    else:
        if stand_R and isJump:
           win.blit(jump_r[animCount // 15], (x,y))
           animCount += 1
        elif stand_L and isJump:
           win.blit(jump_l[animCount // 15], (x,y))
           animCount += 1
        elif stand_R and push:
            win.blit(pushr[pushCount // 15], (x,y))
            pushCount += 1
        elif stand_R and shoot_arrow:
            win.blit(Shoot_arrow_R[shootCount // 6], (x,y))
            shootCount += 1
        elif stand_L and shoot_arrow:
            win.blit(Shoot_arrow_L[shootCount // 6], (x,y))
            shootCount += 1
        elif stand_R and shoot_arrow_p:
            win.blit(Shoot_arrow_p_R[shootCount_p // 6], (x,y))
            shootCount_p += 1
        elif stand_L and shoot_arrow_p_2:
            win.blit(Shoot_arrow_p_L[shootCount_p_2 // 6], (x,y))
            shootCount_p_2 += 1
        elif stand_R and push_h:
            win.blit(push_hand_R[handCount // 15], (x,y))
            handCount += 1
        elif stand_L and push_h:
            win.blit(push_hand_L[handCount // 15], (x,y))
            handCount += 1 
        elif stand_L and push:
            win.blit(pushl[pushCount // 15], (x,y))
            pushCount += 1
        elif stand_R and gg_sead:
            win.blit(sead_r[seadCount// 30], (x,y))
            seadCount += 1
        elif stand_L and gg_sead:
            win.blit(sead_l[seadCount// 30], (x,y))
            seadCount += 1
        else:
            if stand_R or right:
                win.blit(playerStand_R, (x,y))

            if stand_L or left:
                win.blit(playerStand_L, (x,y))
            else:
                win.blit(playerStand_R, (x,y))
        for bullet in bullets:
            bullet.draw(win)
    pygame.display.update()
bullet = snaryad(10,650,0)
zek = enemy(200, 650, 90, 106,1000,10)
hp = medic(800, 700, 70, 60)
hp_2 = medic(800, 700, 70, 60)
run = True
show_menu = True
bullets = []
enemys = []
count_medcit = 0
while run:
    while show_menu:
        if show_menu:
            menu()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        show_menu = False
                    else:
                        pygame.quit()
    
    clock.tick(30)  
    for zek in enemys:
        if zek.health <= 0:
            enemys.pop(enemys.index(zek))
    if len(enemys) < 1:
        enemys.append(enemy(200,650,90,106,1000,10))
        
    if y < hp.hitbox_med[1] + hp.hitbox_med[3] and y + height > hp.hitbox_med[1]:
        if x + hp.hitbox_med[2] > hp.hitbox_med[0] and x < hp.hitbox_med[0] + hp.hitbox_med[2]:
            take.play()
            if hp.visible:
                count_medcit += 1
                hp.visible = False
            else:
                take.stop()
            if not hp.visible:
                count_medcit == count_medcit
                
    if y < hp_2.hitbox_med[1] + hp_2.hitbox_med[3] and y + height > hp_2.hitbox_med[1]:
        if x + hp_2.hitbox_med[2] > hp_2.hitbox_med[0] and x < hp_2.hitbox_med[0] + hp_2.hitbox_med[2]:
            take.play()
            if hp_2.visible:
                count_medcit += 1
                hp_2.visible = False
            else:
                take.stop()
            if not hp.visible:
                count_medcit == count_medcit
                  
    if y < zek.hitbox_zek[1] + zek.hitbox_zek[3] and y + height > zek.hitbox_zek[1]:
            if x + zek.hitbox_zek[2] > zek.hitbox_zek[0] and x < zek.hitbox_zek[0] + zek.hitbox_zek[2]:
                hit_gg()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    for bullet in bullets:
        if bullet.hitbox_arrow[1] < zek.hitbox_zek[1] + zek.hitbox_zek[3] and bullet.hitbox_arrow[1] + bullet.hitbox_arrow[3] > zek.hitbox_zek[1]:
            if bullet.hitbox_arrow[0] + zek.hitbox_zek[2] > zek.hitbox_zek[0] and bullet.hitbox_arrow[0] < zek.hitbox_zek[0] + zek.hitbox_zek[2]:
                zek.hit()
                score += 20
                bullets.pop(bullets.index(bullet))
        if bullet.x < 1360 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        if count_medcit > 0:
            use_medcit.play()
            gg_health = 100
            count_medcit -= 0.5
        else:
            gg_health == gg_health
            count_medcit == count_medcit
        if count_medcit < 0:
            count_medcit = 0

    if keys[pygame.K_t]:
        if y < zek.hitbox_zek[1] + zek.hitbox_zek[3] and y + height > zek.hitbox_zek[1]:
            if x + zek.hitbox_zek[2] > zek.hitbox_zek[0] and x < zek.hitbox_zek[0] + zek.hitbox_zek[2]:
                zek.hit_push()
                score += 10
    if keys[pygame.K_r]:
        if y < zek.hitbox_zek[1] + zek.hitbox_zek[3] and y + height > zek.hitbox_zek[1]:
            if x + zek.hitbox_zek[2] > zek.hitbox_zek[0] and x < zek.hitbox_zek[0] + zek.hitbox_zek[2]:
                zek.hit_push()
                score += 10
                
    if keys[pygame.K_j] and not keys[pygame.K_LCTRL]:
        if not(stand_R):
            facing = -1
        else:
            facing = 1
        if len(bullets) < 1:
            if not (right)and not(left) and not(push) and not(push_h) and not(isJump):
                bullets.append(snaryad(round(x + width // 2) , round(y + height // 4), facing))
    if keys[pygame.K_f]:
        if not(stand_L):
            facing = 1
        else:
            facing = -1
        if len(bullets) < 1:
            if not (right)and not(left) and not(gg_sead) and not(push) and not(push_h) and not(isJump):
                bullets.append(snaryad(round(x + width // 2) , round(y + height // 4),facing))
    if not(isJump):
            if not (right)and not(left) and not(gg_sead) and not(push) and not(push_h):
                if keys[pygame.K_f]:
                    shoot_arrow = True
                    push = False
                    left = False
                    right = False
                    gg_sead = False
                    isJump = False
                    push_h = False
                    pusher.stop()
                    jump.stop()
                    push_m.stop()
                    go.stop()
                    shoot_bow_1.play()
                    sead_sound = False
                else:
                    shoot_bow_1.stop()
                    shoot_arrow = False
                    shootCount = 0
    if not(isJump):
        if not (right)and not(left) and not(gg_sead):
            if keys[pygame.K_r]:
                push_m.play()
                left = False
                right = False
                push = True
                isJump = False
                gg_sead = False
                animCount = 0
            else:
                push = False
                pushCount = 0
                push_m.stop()
                
            if keys[pygame.K_t]:
                pusher.play()
                left = False
                right = False
                push_h = True
                isJump = False
                gg_sead = False
                animCount = 0
            else:
                push_h = False
                handCount = 0
                pusher.stop()
    if not gg_sead:
        if keys[pygame.K_LEFT]  and x > 5:
            go.play()
            scrollX(bg, speed)
            x -= speed
            stand_R = False
            stand_L = True
            gg_sead = False
            left = True
            right = False
            push = False
        elif keys[pygame.K_RIGHT] and x < 1024 - width - 5:
            go.play()
            scrollX(bg, -speed)
            stand_R = True
            stand_L = False
            gg_sead = False
            x += speed
            left = False
            right = True
            push = False
        else:
            go.stop()
            left = False
            right = False
            animCount = 0
        if not(isJump):
            if not (right)and not(left) and not(push) and not(push_h) and not(gg_sead):
                if keys[pygame.K_j]:
                    shoot_arrow_p = True
                    shoot_arrow_p_2 = True
                    gg_sead = False
                    push = False
                    left = False
                    right = False
                    isJump = False
                    push_h = False
                    pusher.stop()
                    jump.stop()
                    push_m.stop()
                    go.stop()
                    shoot_bow_2.play(-1)
                    sead_sound = True
                else:
                    shoot_arrow_p = False
                    shoot_arrow_p_2 = False
                    shoot_bow_2.stop()
                    shootCount_p = 0  
    if not(isJump) and not(left) and not(right) and not(push) and not(push_h):
        if keys[pygame.K_LCTRL]:
            if sead_sound and gg_sead:
                sead.play()
                sead_sound = False
            shoot_arrow_p = False
            shoot_arrow_p_2 = False
            right = False 
            left = False
            push = False
            isJump = False
            gg_sead = True
            shoot_bow_2.stop()
            y = 670
        else:
            sead_sound = True
            y = 650
            gg_sead = False
            seadCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            jump.play()
            shoot_bow_2.stop()
            shoot_bow_1.stop()
            push = False
            isJump = True
            gg_sead = False
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 1.9
            else:
                y -= (jumpCount ** 2) / 1.9
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
            jump.stop()
    drawWindow()
pygame.quit()
