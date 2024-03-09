import pygame

class GameBall():
    def __init__(self) -> None:
        self.ball_pos = pygame.Vector2(640,600)
        self.ball_color = "white"
        
        
    def draw_ball(self,screen):
        pygame.draw.circle(screen, self.ball_color, self.ball_pos, 10)