# -*- coding: utf-8 -*-
from pygame import sprite, image, transform


class Projectile(sprite.Sprite):
    """
    blablabla
    """

    def __init__(self, player):
        super().__init__()
        self.velocity = 6
        self.player = player
        self.image = image.load("assets/projectile.png")
        self.image = transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        """ Blabla """
        # Tourner le projectile en deplacement.
        self.angle -= 3
        self.image = transform.rotozoom(self.origin_image,
                                                    self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        """ Blabla """
        self.player.all_projectiles.remove(self)

    def move(self):
        """ Blabla """
        self.rect.x += self.velocity
        self.rotate()

        # Verifier si le projectile n'est pas en collision avec un monstre.
        for monster in self.player.game.check_collision(
                                    self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

        # Verifier si le projectile n'est pas en dehors de l'ecran.
        if self.rect.x > 2200:
            self.remove()
