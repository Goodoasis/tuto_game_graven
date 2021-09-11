# -*- coding: utf-8 -*-
from random import randint

from pygame import draw

import animation


class Monster(animation.AnimateSprite):
    """
    blabla
    """

    def __init__(self, game, name, size, offset=0, point=20):
        """ Blabla """
        super().__init__(name, size)
        self.offset = offset
        self.point = point
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + randint(0, 300)
        self.rect.y = 540 + randint(-10, 30) - offset
        self.velocity = 3
    
    def cross_limit(self):
        # Tuer les monstres qui sortent de l'écran.
        if self.rect.x <= -250:
            self.damage(100)

    def damage(self, amount):
        # Infliger les degats.
        self.health -= amount
        # Verifier si les points de vie sont a 0.
        if self.health <= 0:
            # Réapparaitre.
            self.rect.x = 1000 + randint(0, 300)
            self.rect.y = 540 + randint(-10, 30) - self.offset
            self.health = self.max_health
            self.velocity = randint(1, self.velocity)
            self.game.score += self.point

            # Si la barre d'evenement est chargé a fond:
            if self.game.comet_event.is_full_loaded():
                # Retire du jeu.
                self.game.all_monsters.remove(self)
                # Appel de la méthode pour essayer de déclencher la pluie de comettes.
                self.game.comet_event.attempt_fall()
    
    def update_animation(self):
        self.animation = True
        self.animate()

    def update_health_bar(self, surface):
        """ Blabla """
        # definir couleur de la jauge de vie (vert et gris).
        bar_color = (111, 210, 46)
        back_bar_color = (70, 70, 70)

        # Definir la position de la jauge ansi que largeur et épaisseur.
        back_bar_position = [self.rect.x+13, self.rect.y-10,
                             self.max_health, 5]
        bar_position = [self.rect.x+13, self.rect.y-10, self.health, 5]
        # Dessiner les jauges
        draw.rect(surface, back_bar_color, back_bar_position)
        draw.rect(surface, bar_color, bar_position)

    def forward(self):
        """Fait avancer le monstre vers la gauche à condition
        qu'il ne soit pas en contact avec le joueur"""
        # le deplacement ne se fait que s'il ne y pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.velocity = 3


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.attack = 0.8
        self.max_health = 250
        self.velocity = 1
        self.point = 40