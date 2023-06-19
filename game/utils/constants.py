import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SOUND_EXPLOSION = os.path.join(IMG_DIR, "Sounds/explosion.mp3")
SOUND_EXPLOSION_PLAYER = os.path.join(IMG_DIR, "Sounds/piu.mp3")
SOUND_BULLET_PLAYER = os.path.join(IMG_DIR, "Sounds/laser.mp3")
SOUND_BULLET_ENEMY = os.path.join(IMG_DIR, "Sounds/laser_2.mp3")
AKU_AKU = os.path.join(IMG_DIR, "Sounds/aku.mp3")
KABOOM = os.path.join(IMG_DIR, "Sounds/explosion_1.mp3")
UP1= os.path.join(IMG_DIR, "Sounds/mario_guwqdsC.mp3")
SOUND_BACK = os.path.join(IMG_DIR, "Sounds/musicafondojuego.MP3")
SOUND_BACK_M = os.path.join(IMG_DIR, "Sounds/fondojuegomenu.MP3")


SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/escudo.png'))

EXPLOSION_ANIM = []
for i in range (1,13):
    file = 'Other/{}.png'.format(i)
    img = pygame.image.load(os.path.join(IMG_DIR,file))
    img = pygame.transform.scale(img,(40,40))
    EXPLOSION_ANIM.append(img)

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

IMG_M = pygame.image.load(os.path.join(IMG_DIR, 'Other/FondoMenu.png'))
IMG_S = pygame.image.load(os.path.join(IMG_DIR, 'Other/fondoscore.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/1up.png'))
MISILE = pygame.image.load(os.path.join(IMG_DIR, 'Other/petaseta.png'))

FONT_STYLE = 'freesansbold.ttf'
