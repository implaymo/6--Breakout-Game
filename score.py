from blocks import Block
import pygame

class NewScore:
    def __init__(self) -> None:
        self.font_initialization = pygame.font.init()
        self.font = pygame.font.Font(None, 36)
            
    def render_score(self, block: Block):
        text_surface = self.font.render(f"Score: {block.block_hit_count}", True, (255, 255, 255))  # Render score text
        return text_surface