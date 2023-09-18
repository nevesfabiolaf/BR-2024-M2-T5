import random
import pygame

from dino_runner.utils.constants import HEART_TYPE, MAX_TYPE
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.components.power_ups.maxspeed import MaxSpeed


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
  
    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(100, 200)
            random_power_up = random.choice(["MaxSpeed", "Heart", "Shield", "Hammer"])
            if random_power_up == "MaxSpeed":
                self.power_ups.append(MaxSpeed())
            elif random_power_up == "Heart":
                self.power_ups.append(Heart())
            elif random_power_up == "Shield":
                self.power_ups.append(Shield())  
            else:
                self.power_ups.append(Hammer())
            
    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
                
                if game.player.type == HEART_TYPE and game.player.has_power_up:
                    game.game_speed = 20
                elif game.player.type == MAX_TYPE and game.player.has_power_up:
                    game.game_speed = game.game_speed + 5
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)
        