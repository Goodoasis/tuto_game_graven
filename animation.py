from pygame import sprite, image, transform

class AnimateSprite(sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = image.load(f"assets\\{sprite_name}.png")
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False
        self.image = transform.scale(self.image, size)

    def start_animation(self):
        self.animation = True
 
    def animate(self):
        """ defninir une methodee pour animer. """
        if self.animation:
            self.current_image +=1
            # Verifier si on arrive a la fin.
            if self.current_image >= len(self.images):
                # REmettre l'animation a la fin
                self.current_image = 0
                self.animation = False
            self.image = self.images[self.current_image]
            self.image = transform.scale(self.image, self.size)

def load_animations_images (sprite_name):
    """ fonction pour charger les images des animations. """
    # Charger les images des dossiers.
    images = []
    path = f"assets\{sprite_name}\{sprite_name}"
    for num in range(1, 24):
        image_path = f"{path}{num}.png"
        images .append(image.load(image_path))
    return images


# Dictionnaire contenant les images de chaques sprites
animations = {
    "mummy": load_animations_images("mummy"),
    "player": load_animations_images("player"),
    "alien": load_animations_images("alien")
}