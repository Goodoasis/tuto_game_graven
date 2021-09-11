from pygame import mixer

class SoundManager():

    def __init__(self):
        self.sounds = {
            'game_over': mixer.Sound("assets\sounds\game_over.ogg"),
            'click': mixer.Sound("assets\sounds\click.ogg"),
            'tir': mixer.Sound("assets\sounds\\tir.ogg"),
            'meteorite': mixer.Sound("assets\sounds\meteorite.ogg")
             }
    
    def play(self, name):
        self.sounds[name].play()