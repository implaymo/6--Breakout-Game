from blocks import Block
import pygame

class NewScore:
    def __init__(self) -> None:
        self.font_initialization = pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.current_highscore = 0
            
    def render_score(self, block: Block):
        score_text = self.font.render(f"Score: {block.block_hit_count}", True, (255, 255, 255))  # Render score text
        return score_text
    
    def render_highscore(self):
        highscore_text = self.font.render(f"Highscore: {self.current_highscore}", True, (255, 255, 255))  # Render score text
        return highscore_text
        
    
    def high_score(self, block: Block):
        try:
            with open("highscore_storage.txt", "r") as file:
                self.current_highscore = file.read()
                if int(self.current_highscore) < block.block_hit_count:
                    with open("highscore_storage.txt", "w") as file:
                        file.write(str(block.block_hit_count))       
        except FileNotFoundError:
            with open("highscore_storage.txt", "w") as file:
                file.write(str(block.block_hit_count))

                

    
            
        