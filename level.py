import pygame

class NewLevel:
    def __init__(self) -> None:
        self.level = 1

    def change_level(self):
        self.level += 1
        