from pygame import sprite, draw

from comet import Comet


class CometFallEvent:
    def __init__(self, game):
        self.fall_mode = False
        self.game = game
        self.percent = 0
        self.percent_speed = 33

        # Definir un groupe de comet
        self.all_comets = sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed /100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent (self):
        self.percent = 0
        self.fall_mode = False
    
    def meteor_fall (self):
        for i in range(10):
            self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.fall_mode = True
            self.meteor_fall()
    
    def update_bar(self, surface):
        # Increment percent
        self.add_percent()

        # Bar noire en arriere plan
        draw.rect(surface, (0, 0, 0), [
            0, 
            surface.get_height() -20, # la hauteur
            surface.get_width(), # la longueur
            10 # Epaisseur de la bar
        ])

        # Barre Rouge 
        draw.rect(surface, (187, 11, 11), [
            0, 
            surface.get_height() -20, # la hauteur
            (surface.get_width() /100)* self.percent, # la longueur
            10 # Epaisseur de la bar
        ])