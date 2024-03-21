from blocks import Block
import pygame

class NewScore:
    def __init__(self) -> None:
        self.font_initialization = pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.highest_score = 0
            
    def render_score(self, block: Block):
        text_surface = self.font.render(f"Score: {block.block_hit_count}", True, (255, 255, 255))  # Render score text
        return text_surface
    
    def high_score(self, block: Block):
        try:
            with open("highscore_storage.txt", "r") as file:
                self.highest_score = int(file.readline())
        except FileNotFoundError:
            print("Error: High score file not found")

        if block.block_hit_count > self.highest_score:
            try:
                with open("highscore_storage.txt", "w") as file:
                    file.write(str(block.block_hit_count))
            except Exception as e:
                print(f"Error updating high score: {e}")
    
            
        