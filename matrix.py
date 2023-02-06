import os
import pygame as pg
import random

# Define the Character class that represents an individual character
class Character:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.value = random.choice(green_katakana)
        self.interval = random.randrange(5, 30)
        
    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = random.choice(green_katakana if color == 'green' else lightgreen_katakana)
        if self.y >= HEIGHT:
            self.y = -FONT_SIZE
        else:
            self.y += self.speed
        surface.blit(self.value, (self.x, self.y))

# Define the CharacterColumn class that represents a column of characters
class CharacterColumn:
    def __init__(self, x, y):
        self.column_height = random.randrange(8, 24)
        self.speed = random.randrange(3, 7)
        self.symbols = [Character(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]
        
    def draw(self):
        for i, symbol in enumerate(self.symbols):
            if i == 0:
                symbol.draw('lightgreen')
            else:
                symbol.draw('green')

# Initialize Pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1920, 1080
FONT_SIZE = 30
alpha_value = 0
pg.init()
screen = pg.display.set_mode(RES, pg.NOFRAME, pg.FULLSCREEN, display=1)
surface = pg.Surface(RES)
surface.set_alpha(alpha_value)
clock = pg.time.Clock()

# Create lists of rendered katakana characters in green and light green
katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.Font('font/ms mincho.ttf', FONT_SIZE, bold=True)
green_katakana = [font.render(char, True, (40, random.randrange(160, 256), 40)) for char in katakana]
lightgreen_katakana = [font.render(char, True, pg.Color('lightgreen')) for char in katakana]

# Create a list of SymbolColumn objects
symbol_columns = [CharacterColumn(x, random.randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

# Main game loop
while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))
    [symbol_column.draw() for symbol_column in symbol_columns]
    if not pg.time.get_ticks() % 20 and alpha_value < 175:
        alpha_value += 4
        if alpha_value <= 100:
            surface.set_alpha(alpha_value)
        else:
            alpha_value = 100
            surface.set_alpha(alpha_value)
    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)