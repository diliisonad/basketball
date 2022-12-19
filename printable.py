import pygame

class Printable:
    '''Класс  для ...'''
    def print(self):
        ''' печатет ... '''
        self.screen.blit(self.image, self.position)

    def move(self, position:int):
        ''' передвигает
        position - целые число от 1 до 4'''
        self.position = position