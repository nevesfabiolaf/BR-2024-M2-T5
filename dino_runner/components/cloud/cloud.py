import pygame
import random
from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(50, 200)

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH + random.randint(300, 1000)
            self.rect.y = random.randint(50, 200)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
