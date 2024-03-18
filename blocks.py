import pygame
import random
from ball import GameBall

class Block():
    def __init__(self) -> None:
        self.block_height = 50
        self.block_width = 81
        self.rows = 3
        self.columns = 15
        self.get_random_color()
        self.all_blocks = []
        self.hit_bottom = False
        self.hit_left_block = False
        self.hit_right_block = False
        
        
    def create_all_block_rects(self):
        for row in range(self.rows):
            for column in range(self.columns):
                block_pos_x = 0 + column * (self.block_width + 5)
                block_pos_y = 100 + row * (self.block_height + 5)
                block_rect = pygame.Rect(block_pos_x, block_pos_y, self.block_width, self.block_height)
                self.all_blocks.append(block_rect)
        
        
    def draw_multiple_blocks(self, screen):
        for block_rect in self.all_blocks:
            pygame.draw.rect(screen, self.color, block_rect)
    
    def check_collision_with_ball(self, ball: GameBall):
        for block in self.all_blocks[:]: 
            if block.colliderect(ball.ball_rect):
                # Check if the ball is hitting the sides of the block
                if (ball.ball_rect.centerx < block.left or ball.ball_rect.centerx > block.right) and ball.ball_speed[0] != 0:
                    # Ball hits the left or right side of the block
                    ball.ball_speed[0] *= -1
                else:
                    # Ball hits the top or bottom of the block
                    ball.ball_speed[1] *= -1
                self.all_blocks.remove(block)
                            
            
            

    
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
            


        
    