import pygame
from player import Player
from rocket import Rocket
class Game:

    def __init__(self):
        # Joueur
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        WHITE = (255, 255, 255)
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.pressed = {}
        # Groupe de rocket
        self.all_rocket = pygame.sprite.Group()
        self.spawn_rocket()
        self.spawn_rocket()
        self.spawn_rocket()

    def spawn_rocket(self):
        rocket = Rocket(self)
        self.all_rocket.add(rocket)
        if rocket.rect.x > 0:
            self.all_rocket.add(rocket)

    # Comparaison de la collision
    def check_collison(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group,False, pygame.sprite.collide_mask)

