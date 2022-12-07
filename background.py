import pygame
import pyautogui

import math

width, height = pyautogui.size()
screen = pygame.display.set_mode((width, height))
white = (255, 255, 255)


class Background():
    def __init__(self, x, y):
        self.surface = pygame.image.load('images/background.png')
        self.surface = pygame.transform.scale(self.surface, (width, height)).convert_alpha()
        self.mg_surface = pygame.image.load('images/midground.png')
        self.mg_surface = pygame.transform.scale(self.mg_surface, (width, height / 2)).convert_alpha()
        self.scroll = 0
        self.tiles = math.ceil(width / self.surface.get_width()) + 1
        self.bg1 = 0
        self.bg2 = self.surface.get_width()
        self.mg1 = 0
        self.mg2 = self.mg_surface.get_width()
        self.game_font = pygame.font.Font('ocrb.ttf', 25)

        self.title_x = 720
        self.title_y = 0

        self.select = False
        self.instruct = False
        self.music = False

        self.again = True
        self.again1 = False
        self.again2 = False
        self.again3 = False

        self.page = 0

        self.unpause = False

    def draw(self):

        self.bg1 -= 1
        self.bg2 -= 1

        if self.bg1 < self.surface.get_width() * -1:
            self.bg1 = self.surface.get_width()

        if self.bg2 < self.surface.get_width() * -1:
            self.bg2 = self.surface.get_width()

        self.mg1 -= 1.5
        self.mg2 -= 1.5

        if self.mg1 < self.mg_surface.get_width() * -1:
            self.mg1 = self.mg_surface.get_width()

        if self.mg2 < self.mg_surface.get_width() * -1:
            self.mg2 = self.mg_surface.get_width()

        pygame.draw.rect(screen, white, (0, 0, width, height))
        screen.blit(self.surface, (self.bg1, 0))
        screen.blit(self.surface, (self.bg2, 0))
        screen.blit(self.mg_surface, (self.mg1, height / 2))
        screen.blit(self.mg_surface, (self.mg2, height / 2))

    def timer(self, start_time):
        game_font = pygame.font.Font('ocrb.ttf', 25)

        counting_time = pygame.time.get_ticks() - start_time
        counting_minutes = str(int(counting_time / 60000)).zfill(2)
        counting_seconds = str(int((counting_time % 60000) / 1000)).zfill(2)

        counting_string = "%s:%s" % (counting_minutes, counting_seconds)

        counting_text = game_font.render(str(counting_string), True, (0, 0, 0))
        counting_rect = counting_text.get_rect(midbottom=(width / 2, 50))

        screen.blit(counting_text, counting_rect)


    def starting_bg(self):
        starting_bg = pygame.image.load('./images/starting_bg.png')
        starting_bg = pygame.transform.scale(starting_bg, (width, height)).convert_alpha()
        screen.blit(starting_bg, (0, 0))

    def ending_bg(self, type):

        if type == "player_death":
            ending_bg = pygame.image.load('./images/death_bg.png')
            text = self.game_font.render('', True, 'black')
        else:
            ending_bg = pygame.image.load('./images/win_bg.png')
            text = self.game_font.render('XBox Membership: CODE HERE CODE.', True, 'black')
        ending_bg = pygame.transform.scale(ending_bg, (width, height)).convert_alpha()
        screen.blit(ending_bg, (0, 0))
        screen.blit(text, (width - 675, height - 150))

    def instructions(self):
        instructions = pygame.image.load('./images/instructions_bg.png')
        text1 = self.game_font.render('1. Use arrows or WASD to avoid the oncoming attacks.', True, 'black')
        text2 = self.game_font.render('2. Use SPACE to attack. Hold it down for continuous attacks.', True, 'black')
        text3 = self.game_font.render('3. Use X/B to parry the blue attacks. Get to five to power up.', True, 'black')
        text4 = self.game_font.render('4. Use C/N and V/M to switch between weapons.', True, 'black')
        text5 = self.game_font.render('5. Switch background music using number keys (0 for selection menu).', True, 'black')
        text6 = self.game_font.render('6. Press H to return to menu screen at any paused screen.', True,'black')
        text7 = self.game_font.render('7. Press P to pause the game at any time.', True, 'black')
        text8 = self.game_font.render('8. Defeat the boss without dying to win a prize.', True, 'black')
        text9 = self.game_font.render('PRESS SPACE TO RETURN', True, 'black')
        instructions = pygame.transform.scale(instructions, (width, height)).convert_alpha()
        screen.blit(instructions, (0, 0))
        screen.blit(text1, (100, 250))
        screen.blit(text2, (100, 300))
        screen.blit(text3, (100, 350))
        screen.blit(text4, (100, 400))
        screen.blit(text5, (100, 450))
        screen.blit(text6, (100, 500))
        screen.blit(text7, (100, 550))
        screen.blit(text8, (100, 600))
        screen.blit(text9, (300, 700))

    def music_selection(self):

        instructions = pygame.image.load('./images/music_menu.png')
        text1 = self.game_font.render('1. Retro Saloon (Default)', True, 'black')
        text2 = self.game_font.render('2. Thomas Theme', True, 'black')
        text3 = self.game_font.render('3. James Theme', True, 'black')
        text4 = self.game_font.render('4. Percy Theme', True, 'black')
        text5 = self.game_font.render('5. In the Mood - Glen Miller', True, 'black')
        text6 = self.game_font.render('6. Top of the World (Jazz) - Carpenters', True, 'black')
        text7 = self.game_font.render('7. Its Beginning to Look a Lot Like Christmas', True, 'black')
        text8 = self.game_font.render('8. The Most Wonderful Time of the Year', True, 'black')
        text9 = self.game_font.render('PRESS SPACE TO RETURN', True, 'black')
        instructions = pygame.transform.scale(instructions, (width, height)).convert_alpha()
        screen.blit(instructions, (0, 0))
        screen.blit(text1, (100, 250))
        screen.blit(text2, (100, 300))
        screen.blit(text3, (100, 350))
        screen.blit(text4, (100, 400))
        screen.blit(text5, (100, 450))
        screen.blit(text6, (100, 500))
        screen.blit(text7, (100, 550))
        screen.blit(text8, (100, 600))
        screen.blit(text9, (300, 700))

    def selection_screen(self, player, play, bg2):
        if self.again:

            white = (255, 255, 255)
            pygame.draw.rect(screen, white, (0, 0, width, height))

            text = self.game_font.render('PARRY TO SELECT AN ITEM''', True, 'black')
            screen.blit(text, (width - 900, height - 75))

            hat_cloud = pygame.image.load('./images/hat_cloud.png')
            hat_cloud = pygame.transform.scale(hat_cloud, (400, 300)).convert_alpha()
            hat_rect = hat_cloud.get_rect()
            hat_rect.center = [1000, 500]
            screen.blit(hat_cloud, hat_rect)

            tie_cloud = pygame.image.load('./images/tie_cloud.png')
            tie_cloud = pygame.transform.scale(tie_cloud, (400, 300)).convert_alpha()
            tie_rect = tie_cloud.get_rect()
            tie_rect.center = [350, 250]
            screen.blit(tie_cloud, tie_rect)

            question_cloud = pygame.image.load('./images/question_cloud.png')
            question_cloud = pygame.transform.scale(question_cloud, (150, 100)).convert_alpha()
            question_rect = question_cloud.get_rect()
            question_rect.center = [250, 750]
            screen.blit(question_cloud, question_rect)

            music_cloud = pygame.image.load('./images/music_cloud.png')
            music_cloud = pygame.transform.scale(music_cloud, (150, 100)).convert_alpha()
            music_rect = music_cloud.get_rect()
            music_rect.center = [500, 750]
            screen.blit(music_cloud, music_rect)

            player.move_and_draw()

            if player.rect.y > height - 100:
                player.rect.y = height - 100

            if player.parrying:
                self.select = True
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.select = False
                self.instruct = False
                self.music = False
                # self.again = True

            if (self.select and player.rect.colliderect(tie_rect)) or self.again1:
                play(1, bg2)
                self.again = False
            # elif (self.select and player.rect.colliderect(hat_rect)) or self.again2:
            #     play(2, bg2)
            #     self.again = False
            elif (self.select and player.rect.colliderect(hat_rect)) or self.again3:
                play(2, bg2)
                self.again = False
            elif self.select and player.rect.colliderect(question_rect):
                self.instruct = True
            elif self.select and player.rect.colliderect(music_rect):
                self.music = True

            if self.instruct and self.select:
                self.instructions()
            if self.music and self.select:
                self.music_selection()

            frame = pygame.image.load('./images/frame.png')
            frame = pygame.transform.scale(frame, (width, height)).convert_alpha()
            frame_rect = frame.get_rect()
            screen.blit(frame, frame_rect)

    def story(self, selection_stuff):
        if self.page == 1:
            pg1 = pygame.image.load('./images/page1.png')
            pg1 = pygame.transform.scale(pg1, (width, height)).convert_alpha()
            pg1_rect = pg1.get_rect()
            screen.blit(pg1, pg1_rect)
            text1 = self.game_font.render('"Sir Topham wants us to work on Christmas! I refuse to work!"', True, 'black')
            screen.blit(text1, (width - 1150, height - 175))
        elif self.page == 2:
            pg2 = pygame.image.load('./images/page2.png')
            pg2 = pygame.transform.scale(pg2, (width, height)).convert_alpha()
            pg2_rect = pg2.get_rect()
            screen.blit(pg2, pg2_rect)
            text1 = self.game_font.render('"But Thomas, he\'ll scrap you!"', True, 'black')
            screen.blit(text1, (width - 950, height - 175))
        elif self.page == 3:
            pg3 = pygame.image.load('./images/page3.png')
            pg3 = pygame.transform.scale(pg3, (width, height)).convert_alpha()
            pg3_rect = pg3.get_rect()
            screen.blit(pg3, pg3_rect)
            text1 = self.game_font.render('"I don\'t care! That\'s my Christmas wish."', True, 'black')
            screen.blit(text1, (width - 1000, height - 175))
        elif self.page == 4:
            pg4 = pygame.image.load('./images/page4.png')
            pg4 = pygame.transform.scale(pg4, (width, height)).convert_alpha()
            pg4_rect = pg4.get_rect()
            screen.blit(pg4, pg4_rect)
            text1 = self.game_font.render('"Hm. Seems like he has a lot of spirit!"', True, 'black')
            screen.blit(text1, (width - 1000, height - 175))
        elif self.page == 5:
            pg5 = pygame.image.load('./images/page5.png')
            pg5 = pygame.transform.scale(pg5, (width, height)).convert_alpha()
            pg5_rect = pg5.get_rect()
            screen.blit(pg5, pg5_rect)
            text1 = self.game_font.render('"But to grant his wish, he\'s going to need a driver."', True, 'black')
            screen.blit(text1, (width - 1100, height - 175))
        elif self.page == 6:
            selection_stuff()

        text = self.game_font.render('PRESS SPACE TO CONTINUE', True, 'black')
        screen.blit(text, (width - 900, height - 75))




