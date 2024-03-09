import pygame

class GameBall:
    def __init__(self) -> None:
        self.ball_pos_x = 640
        self.ball_pos_y = 600
        self.ball_pos = pygame.Vector2(self.ball_pos_x, self.ball_pos_y)
        self.ball_color = "white"
        self.ball_flag = True
        self.ball_speed = 3
        
        
    def draw_ball(self,screen):
        pygame.draw.circle(screen, self.ball_color, self.ball_pos, 10)
        
    def move_ball(self):
        if self.ball_flag:
            self.ball_pos.y += self.ball_speed
    