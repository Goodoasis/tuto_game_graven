from random import randint

from pygame import sprite, image


class Comet(sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image  = image.load("assets\comet.png")
        self.rect = self.image.get_rect()
        self.rect.y = - randint(620, 710)
        self.rect.x = randint(-60, 980)
        self.velocity = randint(4, 11)
        self.comet_event = comet_event

    def remove(self):
        # Play sound
        self.comet_event.game.sound_manager.play('meteorite')
        self.comet_event.all_comets.remove(self)

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.fall_mod = False
            self.comet_event.game.launch_monster()

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 535:
            self.remove()

        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
                ):
            self.remove()
            self.comet_event.game.player.damage(20)

