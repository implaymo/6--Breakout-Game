import pygame
import random

class Block():
    def __init__(self) -> None:
        self.block_height = 50
        self.block_width = 51
        self.get_random_color()
        
    def draw_multiple_blocks(self,screen):
        for i in range(23):
            player_pos_x = 0 + i * (self.block_width + 5)
            player_pos_y = 0
            pygame.draw.rect(screen, self.color, pygame.Rect(player_pos_x, player_pos_y, self.block_width, self.block_height))

    def get_random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        if red == 0 and blue == 0 and green == 0:
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            self.color = (red, green, blue)
        else:
            self.color = (red, green, blue)