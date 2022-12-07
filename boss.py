import random

import pygame
import pyautogui

from bullets import Bullets
from bullets import Bullets2

width, height = pyautogui.size()
screen = pygame.display.set_mode((width, height))


class Boss1:
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.health_start = 700
        self.health_remaining = self.health_start

        self.surface = pygame.image.load("images/boss1_open.png")
        self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()
        self.x_speed = 0
        self.y_speed = 10

        self.x = x
        self.y = y
        self.rect = self.surface.get_rect()
        self.rect.center = [self.x, self.y]

        self.last_shot = pygame.time.get_ticks()
        self.bullet_group = pygame.sprite.Group()
        self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack5")
        self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")

        self.top = 0
        self.bottom = height - 400

        self.movement = 0
        self.cooldown1 = 2500
        self.cooldown3 = 3000
        self.cooldown4 = 2500
        self.cooldown5 = 2500

        self.attack4 = 0

        self.last_laugh = pygame.time.get_ticks()

        self.title_x = 720
        self.title_y = 0

    def move_and_draw(self):

        if self.movement == 0:
            self.top = 0
            self.bottom = height - 400
        elif self.movement == 1:
            self.top = 0
            self.bottom = height - 600
        elif self.movement == 2:
            self.top = height - 600
            self.bottom = height - 100
        elif self.movement == 3:
            self.top = 200
            self.bottom = height - 300
        elif self.movement == 4:
            self.top = 150
            self.bottom = height - 500

        if self.rect.top < self.top:
            self.y_speed = 10
            self.movement = random.randrange(0, 5)
        elif self.rect.top > self.bottom:
            self.y_speed = -10
            self.movement = random.randrange(0, 5)

        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        screen.blit(self.surface, self.rect)

    def attack(self, attack_type):
        if attack_type == 1 or attack_type == 2:
            self.surface = pygame.image.load('./images/boss1_open.png')
            self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown1:
                if attack_type == 1:
                    self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack1")
                else:
                    self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack2")
                    self.cooldown1 = 100
                if self.cooldown1 > 450:
                    self.cooldown1 -= 140
                self.bullet_group.add(self.bullet)
                self.last_shot = time_now

        if attack_type == 3:
            self.surface = pygame.image.load('./images/boss1_closed.png')
            self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown3:
                self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack3")
                # self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat")
                if self.cooldown3 > 1500:
                    self.cooldown3 -= 50
                self.bullet_group.add(self.bullet)
                if self.bullet.rect.y > height / 2:
                    self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat")
                    self.bullet_group.add(self.bullet2)
                if self.bullet.rect.y < height / 2:
                    self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
                    self.bullet_group.add(self.bullet2)
                # self.bullet_group.add(self.bullet2)
                self.last_shot = time_now

        if attack_type == 4:
            self.surface = pygame.image.load('./images/boss1_agape.png')
            self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown4:
                self.attack4 += 1
                if self.attack4 % 3 == 0:
                    self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack4c")
                elif self.attack4 % 3 == 2:
                    self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack4b")
                else:
                    self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack4a")

                self.cooldown4 = 900
                self.bullet_group.add(self.bullet)
                self.last_shot = time_now

        if attack_type == 5:
            self.surface = pygame.image.load('./images/boss1_greedy.png')
            self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()

            time_now = pygame.time.get_ticks()

            which_hat = random.randrange(0, 2)
            if time_now - self.last_shot > self.cooldown5:
                if which_hat == 0:
                    self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat")
                else:
                    self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
            if time_now - self.last_shot > self.cooldown5:
                self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack5")
                if self.cooldown5 > 700:
                    self.cooldown5 -= 85
                self.bullet_group.add(self.bullet)
                self.bullet_group.add(self.bullet2)
                self.last_shot = time_now

        self.bullet_group.update()

    def death(self):
        self.surface = pygame.image.load('./images/boss1_dizzy.png')
        self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()
        self.y_speed = 5
        self.x_speed = 2
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        screen.blit(self.surface, self.rect)

    def health_and_attacks(self):
        if self.health_remaining > 0:
            self.move_and_draw()
            if self.health_remaining > self.health_start - self.health_start * (1 / 5):
                self.attack(1)
            elif self.health_remaining > self.health_start - self.health_start * (2 / 5):
                self.attack(3)
            elif self.health_remaining > self.health_start - self.health_start * (3 / 5):
                self.attack(4)
            else:
                self.attack(5)
            self.bullet_group.draw(screen)

    def sounds(self):
        time_now = pygame.time.get_ticks()
        sound = random.randrange(0, 4)
        if time_now - self.last_laugh > 5000:
            if sound == 0:
                soundObj = pygame.mixer.Sound('sounds/buzz_complain.mp3')
                soundObj.play()
            elif sound == 1:
                soundObj = pygame.mixer.Sound('sounds/buzz_angry.mp3')
                soundObj.play()
            elif sound == 2:
                soundObj = pygame.mixer.Sound('sounds/buzz_laugh.mp3')
                soundObj.play()
            else:
                soundObj = pygame.mixer.Sound('sounds/buzz_other.mp3')
                soundObj.play()
            self.last_laugh = time_now

    def boss_name(self):
        boss_name = pygame.image.load('./images/sir_topham.png')
        boss_name = pygame.transform.scale(boss_name, (1000, 250)).convert_alpha()
        boss_rect = boss_name.get_rect()
        boss_rect.center = [self.title_x, self.title_y]
        if self.title_y < 150:
            self.title_y += 5
        else:
            self.title_y += 100
        screen.blit(boss_name, boss_rect)


class Boss2:
    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)

        self.health_start = 800
        self.health_remaining = self.health_start

        self.surface = pygame.image.load("images/boss2_agape.png")
        self.surface = pygame.transform.scale(self.surface, (250, 500)).convert_alpha()
        self.x_speed = 0
        self.y_speed = 10

        self.x = x
        self.y = y
        self.rect = self.surface.get_rect()
        self.rect.center = [self.x, self.y]

        self.last_shot = pygame.time.get_ticks()
        self.last_shotb = pygame.time.get_ticks()
        self.bullet_group = pygame.sprite.Group()
        self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss1_attack5")
        self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
        self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
        self.bullet3 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")

        self.top = 0
        self.bottom = height - 400

        self.warning1 = True
        self.warning2 = False
        self.warning3 = False
        self.warning4 = False
        self.warning5 = False
        self.dashing = True

        self.movement = 0
        self.cooldown1 = 1000
        self.cooldown2 = 2500
        self.cooldown3a = 3000
        self.cooldown3b = 2500
        self.cooldown4a = 2500
        self.cooldown4b = 2500

        self.attack2 = random.randrange(0, 4)
        self.create_wave = True

        self.attack1 = 0

        self.last_laugh = pygame.time.get_ticks()

        self.player = player

        self.title_x = 720
        self.title_y = 0

    def move_and_draw(self): # DONE

        if not self.dashing:
            if self.movement == 0:
                self.top = -500
                self.bottom = height - 300
            elif self.movement == 1:
                self.top = 0
                self.bottom = height
            elif self.movement == 2:
                self.top = 100
                self.bottom = height - 100
            elif self.movement == 3 and self.rect.top > -100 and self.rect.bottom < height + 100:
                self.dashing = True
            else:
                self.top = 300
                self.bottom = height - 300

            if self.rect.top < self.top:
                self.y_speed = 15
                self.movement = random.randrange(0, 5)
            elif self.rect.top > self.bottom:
                self.y_speed = -15
                self.movement = random.randrange(0, 5)
        else:
            if self.warning1:
                self.y_speed = 0
                self.x_speed = -5
                if self.rect.x < width / 2:
                    self.warning2 = True
            if self.warning2:
                self.x_speed = 25
                self.warning1 = False
                if self.rect.x > width - 100:
                    self.warning2 = False
                    self.warning3 = True
            if self.warning3:
                self.x_speed = -75
                if self.rect.x < 0:
                    self.warning3 = False
                    self.warning4 = True
            if self.warning4:
                self.x_speed = 10
                if self.rect.x >= width - 180:
                    self.x_speed = 0
                    self.y_speed = 10
                    self.warning4 = False
                    self.warning5 = True
            if self.warning5:
                self.warning5 = False
                self.warning1 = True
                self.dashing = False
                self.movement = random.randrange(0, 5)

        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        screen.blit(self.surface, self.rect)

    def attack(self, attack_type):
        if attack_type == 1:
            self.surface = pygame.image.load('./images/boss2_agape.png')
            self.surface = pygame.transform.scale(self.surface, (250, 500)).convert_alpha()

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown1:
                self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss2_attack1a")
                self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss2_attack1b")
                self.bullet3 = Bullets(self.rect.centerx, self.rect.top, "boss2_attack1c")

                self.bullet_group.add(self.bullet1)
                self.bullet_group.add(self.bullet2)
                self.bullet_group.add(self.bullet3)
                self.last_shot = time_now

        if attack_type == 2:
            self.surface = pygame.image.load('./images/boss2_spit.png')
            self.surface = pygame.transform.scale(self.surface, (250, 500)).convert_alpha()

            if self.attack2 == 0:
                bullet_top = -100
                bullet_bottom = 900
            elif self.attack2 == 1:
                bullet_top = 100
                bullet_bottom = 1100
            elif self.attack2 == 2:
                bullet_top = -500
                bullet_bottom = 500
            else:
                bullet_top = -300
                bullet_bottom = 700

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown2:
                if self.cooldown2 > 1000:
                    self.cooldown2 -= 50
                self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss2_attack2a")
                self.bullet2 = Bullets(width, bullet_top, "boss2_attack2b")
                self.bullet3 = Bullets(width, bullet_bottom, "boss2_attack2c")
                if self.dashing and self.bullet2.rect.bottom - self.rect.top >= 0:
                    self.bullet1.is_parry = True
                    self.bullet1.image = pygame.image.load("images/white_droplet_parry.png")
                    self.bullet1.image = pygame.transform.scale(self.bullet1.image, (50, 100)).convert_alpha()
                elif self.dashing and self.rect.bottom - self.bullet3.rect.top >= 0:
                    self.bullet1.is_parry = True
                    self.bullet1.image = pygame.image.load("images/white_droplet_parry.png")
                    self.bullet1.image = pygame.transform.scale(self.bullet1.image, (50, 100)).convert_alpha()
                else:
                    self.bullet1.is_parry = False
                    self.bullet1.image = pygame.image.load("images/white_droplet.png")
                    self.bullet1.image = pygame.transform.scale(self.bullet1.image, (50, 100)).convert_alpha()
                self.bullet_group.add(self.bullet1)
                self.bullet_group.add(self.bullet2)
                self.bullet_group.add(self.bullet3)
                self.last_shot = time_now
                self.attack2 = random.randrange(0, 4)

            if self.dashing:
                self.bullet2.rect.x += 10
                self.bullet3.rect.x += 10
            if self.rect.bottom > width / 2:
                self.bullet1.rect.y -= 7
            if self.rect.bottom < width / 2:
                self.bullet1.rect.y += 7

        if attack_type == 3:
            self.surface = pygame.image.load('./images/boss2_agape.png')
            self.surface = pygame.transform.scale(self.surface, (250, 500)).convert_alpha()

            if self.cooldown3a > 750:
                self.cooldown3a -= 2

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown3a:
                self.bullet1 = Bullets2(self.rect.centerx, self.rect.top, "boss2_attack3", self.player)
                self.bullet_group.add(self.bullet1)
                self.last_shot = time_now
            if time_now - self.last_shotb > self.cooldown3b:
                self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss2_attack4a")
                self.bullet_group.add(self.bullet2)
                self.last_shotb = time_now

        if attack_type == 4:
            self.surface = pygame.image.load('./images/boss2_closed.png')
            self.surface = pygame.transform.scale(self.surface, (250, 500)).convert_alpha()

            if self.cooldown4a > 700:
                self.cooldown4a -= 85

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown4a:
                self.bullet = Bullets(self.rect.centerx, self.rect.top, "boss2_attack4a")
                self.bullet_group.add(self.bullet)
                self.last_shot = time_now
                if self.create_wave == False:
                    self.bullet2.rect.y -= 3
            if self.create_wave:
                self.bullet2 = Bullets(0, height, "boss2_attack4b")
                self.bullet_group.add(self.bullet2)
                self.create_wave = False
                self.last_shot = time_now

        self.bullet_group.update()

    def death(self): # DONE
        self.surface = pygame.image.load('./images/boss2_dizzy.png')
        self.surface = pygame.transform.scale(self.surface, (250, 500)).convert_alpha()
        self.y_speed = 5
        self.x_speed = 2
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        screen.blit(self.surface, self.rect)

    def health_and_attacks(self): # DONE
        if self.health_remaining > 0:
            self.move_and_draw()
            if self.health_remaining > self.health_start - self.health_start * (1 / 5):
                self.attack(1)
            elif self.health_remaining > self.health_start - self.health_start * (2 / 5):
                self.attack(2)
            elif self.health_remaining > self.health_start - self.health_start * (3 / 5):
                self.attack(3)
            else:
                self.attack(4)
            self.bullet_group.draw(screen)

    def sounds(self): # DONE
        time_now = pygame.time.get_ticks()
        sound = random.randrange(0, 4)
        if time_now - self.last_laugh > 5000:
            if sound == 0:
                soundObj = pygame.mixer.Sound('sounds/moo1.wav')
                soundObj.play()
            elif sound == 1:
                soundObj = pygame.mixer.Sound('sounds/moo2.wav')
                soundObj.play()
            elif sound == 2:
                soundObj = pygame.mixer.Sound('sounds/moo3.wav')
                soundObj.play()
            else:
                soundObj = pygame.mixer.Sound('sounds/moo4.wav')
                soundObj.play()
            self.last_laugh = time_now

    def boss_name(self):
        boss_name = pygame.image.load('./images/hatt.png')
        boss_name = pygame.transform.scale(boss_name, (1000, 250)).convert_alpha()
        boss_rect = boss_name.get_rect()
        boss_rect.center = [self.title_x, self.title_y]
        if self.title_y < 150:
            self.title_y += 5
        else:
            self.title_y += 100
        screen.blit(boss_name, boss_rect)


class Boss3:
    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)

        self.health_start = 700
        self.health_remaining = self.health_start

        self.surface = pygame.image.load("images/boss3_body.png")
        self.surface = pygame.transform.scale(self.surface, (400, 1000)).convert_alpha()
        self.x_speed = 0
        self.y_speed = 10

        self.x = x
        self.y = y
        self.rect = self.surface.get_rect()
        self.rect.center = [self.x, self.y]

        self.last_shot = pygame.time.get_ticks()
        self.bullet_group = pygame.sprite.Group()
        self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
        self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
        self.bullet3 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
        self.bullet4 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
        self.bullet5 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
        self.bullet6 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")

        self.top = 0
        self.bottom = height - 400

        self.movement = 0
        self.cooldown1 = 2500
        self.cooldown2 = 3000
        self.cooldown3 = 2500
        self.cooldown4 = 2500

        self.attack4 = 0

        self.last_laugh = pygame.time.get_ticks()

        self.title_x = 720
        self.title_y = 0

    def move_and_draw(self):

        if self.movement == 0:
            self.top = 0
            self.bottom = height - 400
        elif self.movement == 1:
            self.top = 100
            self.bottom = height - 300
        elif self.movement == 2:
            self.top = 200
            self.bottom = height - 200
        elif self.movement == 3:
            self.top = 300
            self.bottom = height - 100
        elif self.movement == 4:
            self.top = 400
            self.bottom = height

        if self.rect.top < self.top:
            self.y_speed = 20
            self.movement = random.randrange(0, 5)
        elif self.rect.top > self.bottom:
            self.y_speed = -20
            self.movement = random.randrange(0, 5)

        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        screen.blit(self.surface, self.rect)

    def attack(self, attack_type):
        if attack_type == 1:
            self.surface = pygame.image.load('./images/boss3_body.png')
            self.surface = pygame.transform.scale(self.surface, (400, 1000)).convert_alpha()

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown1:
                # self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss3_attack1a")
                # self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss3_attack1b")
                # self.bullet3 = Bullets(self.rect.centerx, self.rect.top, "boss3_attack1c")
                # self.bullet4 = Bullets(self.rect.centerx, self.rect.top, "boss3_attack1d")
                # self.bullet5 = Bullets(self.rect.centerx, self.rect.top, "boss3_attack1e")
                # self.bullet6 = Bullets(self.rect.centerx, self.rect.top, "boss3_attack1f")
                # self.bullet_group.add(self.bullet1)
                # self.bullet_group.add(self.bullet2)
                # self.bullet_group.add(self.bullet3)
                # self.bullet_group.add(self.bullet4)
                # self.bullet_group.add(self.bullet5)
                # self.bullet_group.add(self.bullet6)
                self.last_shot = time_now

        if attack_type == 3:
            self.surface = pygame.image.load('./images/boss1_closed.png')
            self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown3:
                self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack3")
                # self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat")
                if self.cooldown3 > 1500:
                    self.cooldown3 -= 50
                self.bullet_group.add(self.bullet1)
                if self.bullet1.rect.y > height / 2:
                    self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat")
                    self.bullet_group.add(self.bullet2)
                if self.bullet1.rect.y < height / 2:
                    self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
                    self.bullet_group.add(self.bullet2)
                # self.bullet_group.add(self.bullet2)
                self.last_shot = time_now

        if attack_type == 4:
            self.surface = pygame.image.load('./images/boss1_agape.png')
            self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()

            time_now = pygame.time.get_ticks()
            if time_now - self.last_shot > self.cooldown4:
                self.attack4 += 1
                if self.attack4 % 3 == 0:
                    self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack4c")
                elif self.attack4 % 3 == 2:
                    self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack4b")
                else:
                    self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack4a")

                self.cooldown4 = 900
                self.bullet_group.add(self.bullet1)
                self.last_shot = time_now

        if attack_type == 5:
            self.surface = pygame.image.load('./images/boss1_greedy.png')
            self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()

            time_now = pygame.time.get_ticks()

            which_hat = random.randrange(0, 2)
            if time_now - self.last_shot > self.cooldown5:
                if which_hat == 0:
                    self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat")
                else:
                    self.bullet2 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack_hat2")
            if time_now - self.last_shot > self.cooldown5:
                self.bullet1 = Bullets(self.rect.centerx, self.rect.top, "boss1_attack5")
                if self.cooldown5 > 700:
                    self.cooldown5 -= 85
                self.bullet_group.add(self.bullet1)
                self.bullet_group.add(self.bullet2)
                self.last_shot = time_now

        self.bullet_group.update()

    def death(self):
        self.surface = pygame.image.load('./images/boss3_dizzy.png')
        self.surface = pygame.transform.scale(self.surface, (500, 1000)).convert_alpha()
        self.y_speed = 5
        self.x_speed = 2
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        screen.blit(self.surface, self.rect)

    def health_and_attacks(self):
        if self.health_remaining > 0:
            self.move_and_draw()
            if self.health_remaining > self.health_start - self.health_start * (1 / 5):
                self.attack(1)
            elif self.health_remaining > self.health_start - self.health_start * (2 / 5):
                self.attack(2)
            elif self.health_remaining > self.health_start - self.health_start * (3 / 5):
                self.attack(3)
            else:
                self.attack(4)
            self.bullet_group.draw(screen)

    def sounds(self):
        time_now = pygame.time.get_ticks()
        sound = random.randrange(0, 4)
        if time_now - self.last_laugh > 5000:
            if sound == 0:
                soundObj = pygame.mixer.Sound('sounds/noise1.wav')
                soundObj.play()
            elif sound == 1:
                soundObj = pygame.mixer.Sound('sounds/noise2.wav')
                soundObj.play()
            elif sound == 2:
                soundObj = pygame.mixer.Sound('sounds/noise3.wav')
                soundObj.play()
            else:
                soundObj = pygame.mixer.Sound('sounds/noise4.wav')
                soundObj.play()
            self.last_laugh = time_now

    def boss_name(self):
        boss_name = pygame.image.load('./images/dowager.png')
        boss_name = pygame.transform.scale(boss_name, (1000, 250)).convert_alpha()
        boss_rect = boss_name.get_rect()
        boss_rect.center = [self.title_x, self.title_y]
        if self.title_y < 150:
            self.title_y += 5
        else:
            self.title_y += 100
        screen.blit(boss_name, boss_rect)