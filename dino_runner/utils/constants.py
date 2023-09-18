import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))
DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))
RESTART = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))
CLOUD_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Other/CloudDead.png"))
OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

RUNNING_HEART = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Heart.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Heart.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_HEART = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHeart.png"))
JUMPING_MAX = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpSkate2.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

DUCKING_HEART = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Heart.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Heart.png")),
]

MAX_SPEED = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoSkate.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoSkate2.png")),        
]
SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
MAX = pygame.image.load(os.path.join(IMG_DIR, 'Other/skate.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

DEFAULT_TYPE = "Default"
SHIELD_TYPE = "Shield"
HAMMER_TYPE = "Hammer"
HEART_TYPE = "Heart"
MAX_TYPE = "Max Speed"
