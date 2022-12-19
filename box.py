import pygame
from printable import Printable

class Box(Printable):
    POSITIONS = [(80, 110), (370, 110), (80, 230), (370, 230)]
    def __init__(self, position, size, screen):
        self.screen = screen
        self.position = position
        self.image = pygame.image.load("images/корзиночка.png")
        self.image = pygame.transform.scale(self.image, size)
        self.size = size