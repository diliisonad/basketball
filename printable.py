import pygame

class Printable:

    def move(self, position:int):
        ''' передвигает
        position - целые число от 1 до 4'''
        self.position = position