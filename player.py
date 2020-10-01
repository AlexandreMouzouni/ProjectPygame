import pygame
from rocket import Rocket



class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 3
        self.max_health = 3
        self.velocity = 5
        self.image = pygame.image.load('assets/licorne.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.mouvement = 0

    def move_bottom(self):
        if not self.game.check_collison(self, self.game.all_rocket):
            self.rect.y += self.velocity

    def move_top(self):
        self.rect.y -= self.velocity
