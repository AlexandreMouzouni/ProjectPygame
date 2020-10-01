import pygame
from pygame.locals import *
from game import Game
from rocket import Rocket
#initialiser la librairie
pygame.init()

info = pygame.display.Info()

print(info.current_w)
print(info.current_h)

# Dimension de la licorne
licorneW=50
licorneH=60

pygame.display.set_caption("Licorne Game")

screen = pygame.display.set_mode((800,500),RESIZABLE)

background = pygame.image.load('assets/Background.jpg')
# screen.blit(pygame.transform.scale(background, screen.get_size()), (0, 0))



game = Game()
rocket = Rocket(game)


# boucle du jeu
continuer = 1


while continuer:
    # mettre a jour la fenetre
    screen.blit(pygame.transform.scale(background, screen.get_size()), (0, 0))
    screen.blit(game.player.image, game.player.rect)
    screen.blit(rocket.text_surface_obj, rocket.text_rect_obj)


    for rocket in game.all_rocket:
        rocket.forward()
        rocket.ajouter()
        rocket.scoring()

    game.all_rocket.draw(screen)
    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_top()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height< screen.get_height():
        game.player.move_bottom()

    print(game.player.rect.y)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
            pygame.quit()
        if event.type == pygame.KEYUP :
            game.pressed[event.key] = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

    game.player.rect.y+=game.player.mouvement
