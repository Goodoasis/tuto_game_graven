# -*- coding: utf-8 -*-
import pygame

from player import Player
from monster import Alien, Mummy
from comet_event import CometFallEvent
from sounds import SoundManager



# Creation de la class Game
class Game:
    """
    blabla
    """

    def __init__(self):
        """ Blabla """
        # definir sur le jeu a commencé ou non.
        self.in_jump = False
        self.is_playing = False
        self.max_height = False
        # Generer notre joueur.
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Generer l'evenement.
        self.comet_event = CometFallEvent(self)
        # Generer nos monstres.
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.score = 0
        self.font = pygame.font.Font('assets/Knewave-Regular.ttf', 25)
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True
        self.player.health = self.player.max_health
        self.launch_monster()
    
    def launch_monster(self):
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        # Play sound.
        self.sound_manager.play("game_over")
        # Supprime tout les monstres.
        self.all_monsters = pygame.sprite.Group()
        self.is_playing = False
        # Supprime tout les météorites.
        self.comet_event.all_comets = pygame.sprite.Group()
        # Desactive la pluis de météorites.
        self.comet_event.fall_mode = False
        # Réinitialise la barre des événements.
        self.comet_event.reset_percent()
        self.score = 0
    
    def jump(self):
        # Calcule inversé
        # Si le joueur est en dessous de la hauteur max et qu'on a pas depassé la limite haute, on monte.
        if (self.player.rect.y > self.player.jump_height) and self.max_height is False:
            self.player.jump()
        # Si le joueur atteint la hauteur max.
        if self.player.rect.y <= self.player.jump_height:
            self.max_height = True
        # Si la hauteur limite est atteinte, on tombe.
        if self.max_height:
            self.player.fall()
        # si on atteint le soll
        if self.player.rect.y >= 500:
            self.player.rect.y == 500
            self.in_jump = False
            self.max_height = False

    def update(self, screen):
        # Verifier si le joueur veut aller a droite ou a gauche.
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        
        if self.pressed.get(pygame.K_q) and self.in_jump is False:
            self.in_jump = True
        
        # continue jump
        if self.in_jump:
            self.jump()

        # Appliquer l'image de mon joueur.
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur.
        self.player.update_health_bar(screen)
        self.player.update_animate()

        # Actualiser la barre d'evenement du jeu.
        self.comet_event.update_bar(screen)

        # Recuperer les projectiles du joueur.
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Recupere les monstres.
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
            monster.cross_limit()
        
        # Recupere les cometes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Appliquer l'ensemble des images de mon groupe de projectile.
        self.player.all_projectiles.draw(screen)

        # Appliquer l'ensemble des images de comettes.
        self.comet_event.all_comets.draw(screen)

        # Appliquer l'ensemble des images de mon groupe de monstre.
        self.all_monsters.draw(screen)

        #Afficher le score surl'écran.
        score_text = self.font.render(f"Score: {self.score}", 1,  (0, 0, 0))
        screen.blit(score_text, (20, 20))
    
    def check_collision(self, sprite, group):
        """ Blabla """
        return pygame.sprite.spritecollide(sprite, group, False,
                                           pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class):
        """ Blabla """
        self.all_monsters.add(monster_class.__call__(self))
