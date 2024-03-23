import pygame
from paddle import PaddleRect
from blocks import Block

class NewLevel:
    def __init__(self) -> None:
        self.level = 1

    def change_level(self, paddle: PaddleRect, block: Block):
        self.level += 1
        paddle.change_size_of_paddle(block)
        