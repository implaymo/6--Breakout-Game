import pygame

class PaddleRect:
    def __init__(self) -> None:   
        self.paddle_width = 100
        self.paddle_height = 10
        self.paddle_pos_x = 640 - (self.paddle_width / 2)
        self.paddle_pos_y = 700
        self.paddle_pos = pygame.Vector2(self.paddle_pos_x, self.paddle_pos_y)
        self.keys = pygame.key.get_pressed()
        self.speed = 1000
        

    
    def move_player(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.paddle_pos.x -= self.speed * dt
            if self.paddle_pos.x < 0:
                self.paddle_pos.x = 0
        if keys[pygame.K_d]:
            self.paddle_pos.x += self.speed * dt
            if self.paddle_pos.x > 1280 - self.paddle_width:  
                self.paddle_pos.x = 1280 - self.paddle_width
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.paddle_pos.x, self.paddle_pos.y, self.paddle_width, self.paddle_height))
    
    