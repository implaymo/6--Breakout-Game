import pygame
from window import Screen

class PaddleRect(Screen):
    def __init__(self) -> None:
        super().__init__()        
        self.player_pos = pygame.Vector2(100,700)
        self.player_pos_tuple = (int(self.player_pos.x), int(self.player_pos.y))
        pygame.draw.rect(self.screen, "purple", pygame.Rect(self.player_pos_tuple[0], self.player_pos_tuple[1], 200, 10))
        self.keys = pygame.key.get_pressed()
    
    
    def move_player(self):
        if self.keys[pygame.K_a]:
            self.player_pos.x -= 1000 * self.screen.dt
        if self.keys[pygame.K_d]:
            self.player_pos.x += 1000 * self.screen.dt
    
    