import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "sources")
pict_dir = os.path.join(data_dir, "pictures")
sound_dir = os.path.join(data_dir, "sounds")

TITLE_PATH = os.path.join(pict_dir, "title1.png")

LEVEL_SURFACE_PATH = os.path.join(pict_dir, "brick_wall.jpeg")
LEVELS_CSV_PATH = os.path.join(data_dir, "levels.csv")

IMAGE_WEIGHT_PATH = os.path.join(pict_dir, "weight.png")
IMAGE_BALLOON_PATH = os.path.join(pict_dir, "balloon.png")
IMAGE_BAR_PATH = os.path.join(pict_dir, "bar.png")
IMAGE_BAR_RIGHT_PATH = os.path.join(pict_dir, "bar_right.png")
IMAGE_BAR_LEFT_PATH = os.path.join(pict_dir, "bar_left.png")
IMAGE_BASKET_PATH = os.path.join(pict_dir, "basket.png")
IMAGE_BRICKS_PATH = os.path.join(pict_dir, "bricks.png")
IMAGE_BASKETBALL_PATH = os.path.join(pict_dir, "basketball.png")

SOUND_WINNING_PATH = os.path.join(sound_dir, "Ta Da.wav")
SOUND_FAIL_PATH = os.path.join(sound_dir, "Sad_Trombone.wav")
SOUND_WELCOME_PATH = os.path.join(sound_dir, "Computer_Magic.wav")


BUTTON_PLAY = "Start!"
BUTTON_CHECK = "See how it works!"
BUTTON_RETRY = "Restart level"
BUTTON_INFO = "Instructions"

ITEM_BASKET_WIDTH = 70
ITEM_BASKET_HEIGHT = 70
ITEM_BAR_WIDTH = 150
ITEM_BAR_HEIGHT = 20
ITEM_BRICKS_WIDTH = 100
ITEM_BRICKS_HEIGHT =  30
ITEM_WEIGHT_WIDTH = 45
ITEM_WEIGHT_HEIGHT = 45
ITEM_BASKETBALL_WIDTH = 45
ITEM_BASKETBALL_HEIGHT = 45
ITEM_BALLOON_WIDTH = 50
ITEM_BALLOON_HEIGHT = 120




