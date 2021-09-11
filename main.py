# -*- coding: utf-8 -*-
"""
tutoriel de graven
Ajouter la possibilité de faire des sauts au joueur et donc d'esquiver des monstres. 
(Les monstres qui sortent de l'ecran meurent automatiquement.)

Created on Wed Jun 24 16:10:21 2020
finish: Monday Sept 06 17:40 2021
@author: Goodoasis
"""

from math import ceil

import pygame

from game import Game


pygame.init()

# Generer la fenetre du jeu.
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# Importer l'image d'arriere plan.
background = pygame.image.load("assets/bg.jpg")

# Importer notre banniere.
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = ceil(screen.get_width() / 4)

# Importer l'image du boutton.
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = ceil(screen.get_width() / 3.33)
play_button_rect.y = screen.get_height() / 2 + 5

# Charger notre jeu.
game = Game()
clock = pygame.time.Clock()

running = True

# Boucle de la fenetre de jeu.
while running:
    # Appliquer l'arriere plan.
    screen.blit(background, (0, -200))
    # verifier si notre jeu a commencer.
    if game.is_playing:
        # declencger les instruction de la partie.
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
    # Mettre à jour l'ecran.
    pygame.display.flip()
    # Condition de sortie de jeu.
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Detecter si le joueur presse ou lache une touche.
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Detection de la touche espace
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    game.start()
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play('click')

    clock.tick(60) 