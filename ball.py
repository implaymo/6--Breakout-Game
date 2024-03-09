import pygame
from paddle import PaddleRect

class GameBall:
    def __init__(self) -> None:
        self.ball_pos = pygame.Vector2(640, 600)
        self.ball_color = "white"
        self.ball_flag = True
        self.ball_speed = 3
        
        
    def draw_ball(self,screen):
        pygame.draw.circle(screen, self.ball_color, self.ball_pos, 10)
        
    def move_ball(self):
        if self.ball_flag:
            self.ball_pos.y += self.ball_speed

            
    def check_if_ball_hit_paddle(self, paddle: PaddleRect):
        x_tolerance = 5
        y_tolerance = 5

        # Check if the ball's y-coordinate is within the range of the paddle's y-coordinate
        # and if the ball's x-coordinate is within the bounding box defined by the paddle's x-coordinate and width
        if (paddle.paddle_pos_y - y_tolerance <= self.ball_pos.y <= paddle.paddle_pos_y + y_tolerance
            and paddle.paddle_pos.x - x_tolerance <= self.ball_pos.x <= paddle.paddle_pos.x + paddle.paddle_width + x_tolerance):
            self.ball_speed *= -1
    
    def check_if_ball_hit_top_bottom_edges(self):
        if self.ball_pos.y < 0:
            self.ball_speed *= -1
        elif self.ball_pos.y > 720:
            print("Game Over")
            self.ball_pos.y = 600