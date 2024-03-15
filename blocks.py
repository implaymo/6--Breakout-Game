import pygame
import random
from ball import GameBall

class Block():
    def __init__(self) -> None:
        self.block_height = 20
        self.block_width = 81
        self.rows = 4
        self.columns = 15
        self.get_random_color()

        
    def draw_multiple_blocks(self,screen):
        self.all_blocks = []
        for row in range(self.rows):
            for column in range(self.columns):
                player_pos_x = 0 + column * (self.block_width + 5)
                player_pos_y = 100 + row * (self.block_height + 5)
                new_block = pygame.draw.rect(screen, self.color, pygame.Rect(player_pos_x, player_pos_y, self.block_width, self.block_height))
                self.all_blocks.append(new_block) 
        return self.all_blocks
    
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
            
    def delete_block(self, ball: GameBall):
        for i in self.all_blocks:
            block = self.all_blocks[i]
            if block == ball.ball_pos:
                self.all_blocks.pop(block)
        