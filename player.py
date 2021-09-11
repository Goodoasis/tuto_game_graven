# -*- coding: utf-8 -*-
from pygame import sprite, draw

import animation
from projectile import Projectile


# Creation de la class Player qui representera notre joueur.
class Player (animation.AnimateSprite):
    """
    blabla
    """

    def __init__(self, game):
        """ Blabla """
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.velocity = 5
        self.all_projectiles = sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.jump_height = 500 - 200
        self.gravity = 5
    
    def jump(self):
        velocity = ((self.rect.y - self.jump_height) /100) * 10
        self.rect.y -= (self.gravity + velocity)
    
    def fall(self):
        velocity = ((self.rect.y - self.jump_height) /100) * 4
        self.rect.y += (self.gravity + velocity)
    
    def update_animate(self):
        self.animate()

    def damage(self, amount):
        if (self.health - amount) >= 0:
            self.health -= amount
        else:
            # Si l joeur n'a plus de point de vie.
            self.game.game_over()

    def update_health_bar(self, surface):
        """ Blabla """
        # definir couleur de la jauge de vie (vert et gris).
        bar_color = (133, 223, 67)
        back_bar_color = (50, 50, 50)

        # Definir la position de la jauge ansi que largeur et épaisseur.
        back_bar_position = [self.rect.x+50, self.rect.y+20,
                             self.max_health, 7]
        bar_position = [self.rect.x+50, self.rect.y+20, self.health, 7]

        # Dessiner les jauges.
        draw.rect(surface, back_bar_color, back_bar_position)
        draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        """Fonction du joueur pour lancer un projectile"""
        self.start_animation()
        self.all_projectiles.add(Projectile(self))
        # Play sound.
        self.game.sound_manager.play('tir')

    def move_right(self):
        """ Deplace le joueur sur la droite"""
        # Si le joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        """ Deplace le joueur sur la gauche"""
        self.rect.x -= self.velocity
