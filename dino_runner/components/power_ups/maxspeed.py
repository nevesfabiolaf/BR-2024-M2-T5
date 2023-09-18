from dino_runner.utils.constants import MAX, MAX_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class MaxSpeed(PowerUp):
    def __init__(self):
        self.image = MAX
        self.type = MAX_TYPE
        super().__init__(self.image, self.type)
        