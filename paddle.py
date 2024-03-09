import pygame

class PaddleRect():
    def __init__(self) -> None:   
        self.player_pos = pygame.Vector2(100,700)
        self.paddle_width = 200
        self.paddle_height = 10
        self.keys = pygame.key.get_pressed()
        self.speed = 1000

    
    def move_player(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player_pos.x -= self.speed * dt
            if self.player_pos.x < 0:
                self.player_pos.x = 0
        if keys[pygame.K_d]:
            self.player_pos.x += self.speed * dt
            if self.player_pos.x > 1280 - self.paddle_width:  
                self.player_pos.x = 1280 - self.paddle_width
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.player_pos.x, self.player_pos.y, self.paddle_width, self.paddle_height))
    
    