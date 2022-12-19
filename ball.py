import pygame
from printable import Printable

class Ball(Printable):
    POSITIONS = [
        [(10, 60), (20, 60), (30, 60), (40, 60), (50, 60), (60, 60), (70, 70), (80, 80), (90, 90), (100, 100), (150, 150)],
        [(550, 60), (540, 60), (530, 60), (520, 60), (510, 60), (500, 60), (490, 70), (480, 80), (470, 90), (460, 100), (0, 150)],
        [(10, 180), (20, 180), (30, 180),(40, 180),(50, 180),(60, 180),  (70, 190),(80, 200), (90, 210), (100, 220), (150, 270)],
        [(550, 180), (540, 180), (530, 180), (520, 180), (510, 180), (500, 180), (490, 190), (480, 200), (470, 210), (460, 220), (370, 270)]
    ]

    def __init__(self, position, size, screen):
        self.screen = screen
        self.position = position
        self.image = pygame.image.load("images/ball.png")
        self.image = pygame.transform.scale(self.image, size)
        self.size = size
