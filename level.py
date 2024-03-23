import pygame
from paddle import PaddleRect

class NewLevel:
    def __init__(self) -> None:
        self.level = 1
        self.font_initialization = pygame.font.init()
        self.font = pygame.font.Font(None, 36)

    def change_level(self, paddle: PaddleRect):
        self.level += 1
        paddle.change_paddle_size()
        
    def render_level(self):
        level_text = self.font.render(f"Level: {self.level}", True, (255, 255, 255))  # Render level text
        return level_text
    

