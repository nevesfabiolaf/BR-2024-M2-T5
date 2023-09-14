import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, small_image, large_image):
        self.small_image = small_image
        self.large_image = large_image
        self.type = random.choice(["small", "large"])
        if self.type == "small":
            super().__init__(random.choice(small_image))
            self.rect.y = 325
        else:
            super().__init__(random.choice(large_image))
            self.rect.y = 300
