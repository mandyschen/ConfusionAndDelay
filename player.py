import pygame
import pyautogui
from bullets import Bullets
from background import Background

width, height = pyautogui.size()
screen = pygame.display.set_mode((width, height))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.image.load("images/player1.png")
        self.surface = pygame.transform.scale(self.surface, (125, 125)).convert_alpha()
        self.rect = self.surface.get_rect()
        self.rect.center = [x, y]

        self.x_speed = 15 # 15
        self.y_speed = 25 # 25
        self.gravity = 15 # 15

        self.health_start = 5 #CHANGE THIS BACK TO 5
        self.health_remaining = self.health_start

        self.num_of_parries = 0
        self.last_shot = pygame.time.get_ticks()
        self.bullet_group = pygame.sprite.Group()

        self.cooldown = 200
        self.fast_cooldown = 200
        self.slow_cooldown = 600
        self.attack_type = "player_fast"

        self.parrying = False

        self.bullet = Bullets(self.rect.centerx, self.rect.top, self.attack_type)
        self.strength = 1 # CHANGE THIS BACK TO 1

        self.down_once = False
        self.up_once = True
        self.parry_time = 0
        self.parry_start = pygame.time.get_ticks()
        self.parry_power_time = pygame.time.get_ticks()
        self.parry_power = False

        self.potential_parry1 = 1
        self.potential_parry2 = False

        self.last_attacked = pygame.time.get_ticks()

        self.time_now = pygame.time.get_ticks()

        self.pausing = False

    def move_and_draw(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= self.x_speed
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += self.x_speed
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.y -= self.y_speed
        # if key[pygame.K_DOWN] or key[pygame.K_s]:
        #     self.rect.y += self.y_speed
        self.rect.y += self.gravity

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.bottom > height + 150:
            self.health_remaining -= 1
            soundObj = pygame.mixer.Sound('sounds/get_hit.mp3')
            soundObj.play()
        if self.rect.y < 0:
            self.rect.y = 0

        self.time_now = pygame.time.get_ticks()

        if key[pygame.K_c] or key[pygame.K_n]:
            self.strength = 1
            self.cooldown = self.fast_cooldown
            self.attack_type = "player_fast"
        elif key[pygame.K_v] or key[pygame.K_m]:
            self.strength = 3
            self.cooldown = self.slow_cooldown
            self.attack_type = "player_slow"

        if key[pygame.K_SPACE] and self.time_now - self.last_shot > self.cooldown:
            soundObj = pygame.mixer.Sound('sounds/hitting.mp3')
            soundObj.play()
            self.bullet = Bullets(self.rect.centerx, self.rect.top, self.attack_type)
            self.bullet_group.add(self.bullet)
            self.last_shot = self.time_now
        self.bullet_group.update()

        screen.blit(self.surface, self.rect)

        if key[pygame.K_x] or key[pygame.K_b]:
            # self.potential_parry1 += 1
            self.parrying = True
            self.surface = pygame.image.load("images/player1_parry.png")
            self.surface = pygame.transform.scale(self.surface, (135, 135)).convert_alpha()
            self.parry_time = self.time_now

        if self.time_now - self.parry_time > 500:
            self.parrying = False
            self.surface = pygame.image.load("images/player1.png")
            self.surface = pygame.transform.scale(self.surface, (125, 125)).convert_alpha()

        for i in range(self.num_of_parries):
            item_pic_surface = pygame.image.load('./images/star.png')
            item_pic_surface = pygame.transform.scale(item_pic_surface, (width / 30, height / 30)).convert_alpha()
            item_pic_rect = item_pic_surface.get_rect(center=(width - 100 - (50 * i), 100))
            screen.blit(item_pic_surface, item_pic_rect)

        if self.num_of_parries == 5:
            self.num_of_parries = 0
            self.potential_parry1 = -1
        if self.potential_parry1 == 0:
            self.parry_power_time = self.time_now
            self.parry_power = True

        # print(self.potential_parry1)
        if self.parry_power:
            self.potential_parry1 = 1

        if self.time_now - self.parry_power_time < 1000 and self.parry_power:
            if self.attack_type == "player_fast":
                self.cooldown = self.fast_cooldown / 3
            else:
                self.cooldown = self.slow_cooldown / 3
        else:
            if self.attack_type == "player_fast":
                self.cooldown = self.fast_cooldown
            else:
                self.cooldown = self.slow_cooldown
            self.parry_power = False

    def get_attacked(self, boss):
        for bullet in boss.bullet_group:
            if self.rect.colliderect(bullet.rect):
                if self.parrying and bullet.is_parry:
                    self.num_of_parries += 1
                    soundObj = pygame.mixer.Sound('sounds/parry.mp3')
                    soundObj.play()
                    self.last_attacked = self.time_now
                    bullet.rect.x = -500
                    bullet.kill()
                elif self.time_now - self.last_attacked > 1000:
                    self.surface = pygame.image.load("images/player_damage.png")
                    self.surface = pygame.transform.scale(self.surface, (125, 125)).convert_alpha()
                    self.health_remaining -= 1
                    soundObj = pygame.mixer.Sound('sounds/get_hit.mp3')
                    soundObj.play()
                    self.last_attacked = self.time_now

        if self.rect.colliderect(boss.rect):
            if self.time_now - self.last_attacked > 1000:
                self.surface = pygame.image.load("images/player_damage.png")
                self.surface = pygame.transform.scale(self.surface, (125, 125)).convert_alpha()
                self.health_remaining -= 2
                soundObj = pygame.mixer.Sound('sounds/get_hit.mp3')
                soundObj.play()
                self.last_attacked = self.time_now

        for bullet in self.bullet_group:
            if boss.rect.x - bullet.rect.x < -25 and boss.rect.top - bullet.rect.top <= 0\
                    and boss.rect.bottom - bullet.rect.bottom >= 0:
                bullet.rect.x = -500
                bullet.kill()
                boss.health_remaining -= self.strength

    def basic_keys(self, bg, play, starting, selection_stuff):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE and starting:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_SPACE]:
                        bg.page += 1
                    bg.story(selection_stuff)
                if event.key == pygame.K_h:
                    selection_stuff()
                if event.key == pygame.K_x or event.key == pygame.K_b:
                    self.potential_parry1 += 1
                if event.key == pygame.K_p:
                    self.pausing = not self.pausing
                if event.key == pygame.K_0:
                    bg.music_selection()
                if event.key == pygame.K_1:
                    pygame.mixer.music.load('sounds/bg_music.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                if event.key == pygame.K_2:
                    pygame.mixer.music.load('sounds/thomas_theme.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                if event.key == pygame.K_3:
                    pygame.mixer.music.load('sounds/james_theme.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                if event.key == pygame.K_4:
                    pygame.mixer.music.load('sounds/percy_theme.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                if event.key == pygame.K_5:
                    pygame.mixer.music.load('sounds/essential_glenmiller.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                if event.key == pygame.K_6:
                    pygame.mixer.music.load('sounds/top_of_the_world.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                if event.key == pygame.K_7:
                    pygame.mixer.music.load('sounds/look_like_xmas.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                if event.key == pygame.K_8:
                    pygame.mixer.music.load('sounds/most_wonderful_xmas.mp3')
                    pygame.mixer.music.play(-1, 0.0)

    def display_health(self):
        for i in range(self.health_remaining):
            health_surface = pygame.image.load('./images/heart.png')
            health_surface = pygame.transform.scale(health_surface, (width / 25, height / 25)).convert_alpha()
            health_rect = health_surface.get_rect(center=(width - 100 - (100 * i), 50))
            screen.blit(health_surface, health_rect)




