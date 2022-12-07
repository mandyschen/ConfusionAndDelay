import pygame
import pyautogui
import random
import math

width, height = pyautogui.size()


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        p = random.randrange(0, 4) # (0, 4)
        if p == 0:
            self.is_parry = True
        else:
            self.is_parry = False
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.x_speed = 0
        self.y_speed = 0
        if type == "player_fast":
            self.image = pygame.image.load("images/fast_attack.png")
            self.image = pygame.transform.scale(self.image, (50, 50)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
        elif type == "player_slow":
            self.image = pygame.image.load("images/slow_attack.png")
            self.image = pygame.transform.scale(self.image, (100, 50)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
        elif type == "boss1_attack1" or type == "boss1_attack2":
            if self.is_parry:
                self.image = pygame.image.load("images/white_droplet_parry.png")
            else:
                self.image = pygame.image.load("images/white_droplet.png")
            self.image = pygame.transform.scale(self.image, (100, 100)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [x - 50, y + 200]
        elif type == "boss1_attack3" or type == "boss1_attack3_v":
            if type == "boss1_attack3":
                self.image = pygame.image.load("images/boss1_arm.png")
                self.image = pygame.transform.scale(self.image, (2000, 200)).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.center = [2000, y + 200]
            elif type == "boss1_attack3_v":
                self.image = pygame.image.load("images/boss1_arm_vertical.png")
                self.image = pygame.transform.scale(self.image, (200, 2000)).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.center = [35, 0]
            self.is_parry = False
            self.x_speed = 10
            self.y_speed = 10
            self.recoil = True
        elif type == "boss1_attack_hat":
            self.image = pygame.image.load("images/boss1_hat.png")
            self.image = pygame.transform.scale(self.image, (200, 200)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [0, -550]
            self.is_parry = False
            self.x_speed = 6
            self.y_speed = 15
        elif type == "boss1_attack_hat2":
            self.image = pygame.image.load("images/boss1_hat.png")
            self.image = pygame.transform.scale(self.image, (200, 200)).convert_alpha()
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect()
            self.rect.center = [width - 25, -550]
            self.is_parry = False
            self.x_speed = -15
            self.y_speed = 15
        elif type == "boss1_attack4a" or type == "boss1_attack4b" or type == "boss1_attack4c":
            if type == "boss1_attack4a":
                if self.is_parry:
                    self.image = pygame.image.load("images/get_parry.png")
                else:
                    self.image = pygame.image.load("images/get.png")
            if type == "boss1_attack4b":
                if self.is_parry:
                    self.image = pygame.image.load("images/to_parry.png")
                else:
                    self.image = pygame.image.load("images/to.png")
            if type == "boss1_attack4c":
                if self.is_parry:
                    self.image = pygame.image.load("images/work_parry.png")
                else:
                    self.image = pygame.image.load("images/work.png")
            self.x_speed = 0
            self.y_speed = 0
            self.image = pygame.transform.scale(self.image, (200, 150)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [x - 50, y + 200]
        elif type == "boss1_attack5":
            which_bill = random.randrange(0, 3)
            if which_bill == 0:
                if self.is_parry:
                    self.image = pygame.image.load("images/dollar1_parry.png")
                else:
                    self.image = pygame.image.load("images/dollar1.png")
            elif which_bill == 1:
                if self.is_parry:
                    self.image = pygame.image.load("images/dollar2_parry.png")
                else:
                    self.image = pygame.image.load("images/dollar2.png")
            else:
                if self.is_parry:
                    self.image = pygame.image.load("images/dollar3_parry.png")
                else:
                    self.image = pygame.image.load("images/dollar3.png")
            self.x_speed = 0
            self.y_speed = 10
            self.image = pygame.transform.scale(self.image, (100, 150)).convert_alpha()
            self.rect = self.image.get_rect()
            which_x = random.randrange(0, width - 250)
            self.rect.center = [which_x, 0]
        elif type == "boss2_attack1a" or type == "boss2_attack1b" or type == "boss2_attack1c":
            if self.is_parry:
                self.image = pygame.image.load("images/needle_parry.png")
            else:
                self.image = pygame.image.load("images/needle.png")
            self.x_speed = 0
            self.y_speed = 0
            self.image = pygame.transform.scale(self.image, (200, 100)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [x - 50, y + 200]
        elif type == "boss2_attack2a":
            # self.is_parry = True
            if self.is_parry:
                self.image = pygame.image.load("images/white_droplet_parry.png")
            else:
                self.image = pygame.image.load("images/white_droplet.png")
            self.x_speed = 0
            self.y_speed = 0
            self.image = pygame.transform.scale(self.image, (50, 100)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [x - 50, y + 400]
        elif type == "boss2_attack2b" or type == "boss2_attack2c":
            self.is_parry = False
            if type == "boss2_attack2b":
                self.image = pygame.image.load("images/boss1_arm_v_down.png")
            else:
                self.image = pygame.image.load("images/boss1_arm_v_up.png")
            self.x_speed = 0
            self.y_speed = 0
            self.image = pygame.transform.scale(self.image, (100, 1000)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [x - 50, y + 200]
        elif type == "boss2_attack4a":
            # attack4 = random.randrange(0, 3)
            # if attack4 == 0:
            #     self.is_parry = True
            # else:
            #     self.is_parry = False
            if self.is_parry:
                self.image = pygame.image.load("images/black_droplet_parry.png")
            else:
                self.image = pygame.image.load("images/black_droplet.png")
            self.x_speed = 0
            self.y_speed = 0
            attack4_width = random.randrange(50, 75)
            attack4_height = random.randrange(100, 125)
            self.image = pygame.transform.scale(self.image, (attack4_width, attack4_height)).convert_alpha()
            self.rect = self.image.get_rect()
            which_x = random.randrange(0, width)
            self.rect.center = [which_x, 0]
        elif type == "boss2_attack4b":
            self.image = pygame.image.load("images/wave.png")
            self.x_speed = 0
            self.y_speed = 0
            self.image = pygame.transform.scale(self.image, (width + 100, height + 100)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [width / 2, height + 490]
        elif type == "boss3_attack1a":
            if self.is_parry:
                self.image = pygame.image.load("images/white_droplet_parry.png")
            else:
                self.image = pygame.image.load("images/white_droplet.png")
            self.x_speed = 0
            self.y_speed = 0
            self.image = pygame.transform.scale(self.image, (50, 100)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [x - 50, y + 400]

    def update(self):
        if self.type == "player_fast" or self.type == "player_slow":
            self.rect.x += 50
            if self.rect.right > width + 5000:
                self.kill()
        elif self.type == "boss1_attack1":
            self.rect.x -= 30
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss1_attack2":
            self.rect.x -= 50
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss1_attack3":
            if self.rect.left < 0:
                self.x_speed = 10
                self.y_speed = 10
                self.recoil = False
            elif self.rect.left > 1000 and self.recoil:
                self.x_speed = -100
                self.y_speed = 0
            if self.rect.left > 1500 and not self.recoil:
                self.kill()
        elif self.type == "boss1_attack3_v":
            if self.rect.top > height / 2:
                self.x_speed = 50
                self.y_speed = 10
                self.recoil = False
            elif self.rect.top < 1000 and self.recoil:
                self.x_speed = 0
                self.y_speed = -50
            if self.rect.left > 1500 and not self.recoil:
                self.kill()
        elif self.type == "boss1_attack_hat" or self.type == "boss1_attack_hat2":
            if self.rect.top > height + 500:
                self.kill()
        elif self.type == "boss1_attack4a":
            self.rect.x -= 50
            self.rect.y -= 15
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss1_attack4b":
            self.rect.x -= 50
            self.rect.y += 0
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss1_attack4c":
            self.rect.x -= 50
            self.rect.y += 15
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss1_attack5":
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss2_attack1a":
            self.rect.x -= 30
            self.rect.y -= 15
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss2_attack1b":
            self.rect.x -= 30
            self.rect.y += 0
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss2_attack1c":
            self.rect.x -= 30
            self.rect.y += 15
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss2_attack2a":
            self.rect.x -= 20
            self.rect.y += 0
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss2_attack2b":
            self.rect.x -= 15
            self.rect.y -= 2.5
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss2_attack2c":
            self.rect.x -= 15
            self.rect.y += 2.5
            if self.rect.right < -500:
                self.kill()
        elif self.type == "boss2_attack4a":
            self.rect.x -= 0
            self.rect.y += 15
            if self.rect.top > height + 500:
                self.kill()
        elif self.type == "boss2_attack4b":
            self.rect.x -= 0
            self.rect.y -= 0
            if self.rect.top < -100:
                self.kill()
        elif self.type == "boss3_attack1a": # petal up
            self.rect.x -= 0
            self.rect.y -= 10
            if self.rect.top < -100:
                self.kill()
        elif self.type == "boss3_attack1b": # petal down
            self.rect.x -= 0
            self.rect.y += 10
            if self.rect.top > height + 100:
                self.kill()
        elif self.type == "boss3_attack1c": # petal left
            self.rect.x -= 10
            self.rect.y -= 0
            if self.rect.left < -100:
                self.kill()
        elif self.type == "boss3_attack1d": # petal right
            self.rect.x += 10
            self.rect.y -= 0
            if self.rect.right < width + 100:
                self.kill()
        elif self.type == "boss3_attack1e": # petal center
            self.rect.x -= 10
            self.rect.y -= 0
            if self.rect.top < -100:
                self.kill()
        elif self.type == "boss3_attack1f": # vines
            self.rect.x -= 0
            self.rect.y -= 0
            if self.rect.top < -100:
                self.kill()

        self.rect.y += self.y_speed
        self.rect.x += self.x_speed


class Bullets2(pygame.sprite.Sprite):
    def __init__(self, x, y, type, player):
        self.health_start = 7
        self.health_remaining = self.health_start
        p = random.randrange(0, 4)
        if p == 0:
            self.is_parry = True
        else:
            self.is_parry = False
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.x_speed = 0
        self.y_speed = 0
        self.player = player
        size = random.randrange(100, 250)
        if self.is_parry:
            self.image = pygame.image.load("images/mini_hat_parry.png")
        else:
            self.image = pygame.image.load("images/mini_hat.png")
        self.image = pygame.transform.scale(self.image, (size, size)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [width, y]

        self.floating_point_x = self.rect.x
        self.floating_point_y = self.rect.y

        x_diff = player.rect.x - self.rect.x
        y_diff = player.rect.y - self.rect.y
        angle = math.atan2(y_diff, x_diff);

        velocity = random.randrange(20, 45)
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity

    def update(self):
        if self.type == "boss2_attack3":
            self.floating_point_y += self.change_y
            self.floating_point_x += self.change_x
            self.rect.y = int(self.floating_point_y)
            self.rect.x = int(self.floating_point_x)
            if self.rect.right < -500 or self.rect.left > width + 500:
                self.kill()
            for bullet in self.player.bullet_group:
                if self.rect.colliderect(bullet.rect):
                    self.health_remaining -= 1

            if self.health_remaining <= 0:
                self.kill()

        self.rect.y += self.y_speed
        self.rect.x += self.x_speed





