import pygame
from paddle import PaddleRect

class GameBall:
    def __init__(self) -> None:
        self.ball_pos = pygame.Vector2(640, 660)
        self.ball_color = "white"
        self.ball_speed = [3, 3]
        self.last_hit_right_wall = False
        self.last_hit_left_wall = False
        
        
    def draw_ball(self,screen):
        pygame.draw.circle(screen, self.ball_color, self.ball_pos, 10)
        
    def move_ball(self):
        self.ball_pos -= self.ball_speed

    def ball_hit_left_side_paddle(self, paddle: PaddleRect):
        """Checks if ball hits the left side of the paddle and if it is between boundaries"""
        y_tolerance = 7
        mid_paddle_pos = paddle.paddle_pos.x + (paddle.paddle_width / 2)
        if (paddle.paddle_pos.x <= self.ball_pos.x <= mid_paddle_pos and paddle.paddle_pos.y - y_tolerance <= self.ball_pos.y <= paddle.paddle_pos.y + y_tolerance):
            
            self.move_ball_diagonal_left_up()

    def ball_hit_right_side_paddle(self, paddle: PaddleRect):
        """Checks if ball hits the right side of the paddle and if it is between boundaries"""
        y_tolerance = 7
        mid_paddle_pos = paddle.paddle_pos.x + (paddle.paddle_width / 2)
        right_edge_paddle = paddle.paddle_pos.x + paddle.paddle_width
        if (mid_paddle_pos <= self.ball_pos.x <= right_edge_paddle and paddle.paddle_pos.y - y_tolerance <= self.ball_pos.y <= paddle.paddle_pos.y + y_tolerance):
            
            self.move_ball_diagonal_right_up()


    def check_if_ball_hit_paddle(self, paddle: PaddleRect):
        self.ball_hit_left_side_paddle(paddle)
        self.ball_hit_right_side_paddle(paddle)
            
    
    def check_if_ball_hit_top_bottom_edges(self):
        top = 0
        bottom = 720
        if self.ball_pos.y < top:
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= 1
        elif self.ball_pos.y > bottom:
            print("Game Over")
            self.ball_pos.y = 600
            
    def check_if_ball_hit_side_edges(self):
        left_wall = 0
        right_wall = 1280
        if self.ball_pos.x < left_wall:
            self.last_hit_left_wall = True
            self.last_hit_right_wall = False
            self.ball_speed[0] *= -1
        elif self.ball_pos.x > right_wall:
            self.last_hit_left_wall = False
            self.last_hit_right_wall = True
            self.ball_speed[0] *= -1
            

    def move_ball_diagonal_left_up(self):
        if self.last_hit_left_wall is True:
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= -1
        else:
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= 1
            
            
    def move_ball_diagonal_right_up(self):
        if self.last_hit_right_wall is True:
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= -1
        else: 
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= 1

  
            