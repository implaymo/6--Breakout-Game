import pygame

class PaddleRect():
    def __init__(self) -> None:   
        self.player_pos = pygame.Vector2(100,700)
        self.player_width = 200
        self.player_height = 10
        self.keys = pygame.key.get_pressed()

    
    def move_player(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player_pos.x -= 1000 * dt
        if keys[pygame.K_d]:
            self.player_pos.x += 1000 * dt
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.player_pos.x, self.player_pos.y, self.player_width, self.player_height))
    
    