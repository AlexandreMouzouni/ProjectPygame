import pygame
import random

class Rocket(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        WHITE = (255, 255, 255)
        self.game = game
        self.image = pygame.image.load('assets/rocket.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(780,800)
        self.rect.y = random.randint(0,375)
        self.velocity = random.randint(1,6)
        self.score = 10
        self.font_obj = pygame.font.Font('freesansbold.ttf', 32)
        self.text_surface_obj = self.font_obj.render("SCORE: " + str(self.score), False, GREEN, BLUE)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (90, 20)


    def forward(self):
        # le deplacement continue si il n'y a pas de collision
        if not self.game.check_collison(self, self.game.all_player):
            self.rect.x-= self.velocity

    def ajouter(self):
        if self.rect.x < -200:
            self.rect.x = random.randint(780, 800)
            self.rect.y = random.randint(0, 375)
            self.rect.x -= self.velocity

    def scoring(self):
        if self.rect.x < -200 :
            self.score +=1

