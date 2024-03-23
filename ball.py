import pygame
from paddle import PaddleRect
import random


class GameBall:
    def __init__(self, paddle: PaddleRect) -> None:
        self.ball_start_position(paddle)
        self.ball_pos = pygame.Vector2(self.ball_start_pos, 690)
        self.ball_color = "white"
        self.ball_radius = 5
        self.ball_speed = [5, 5]
        self.last_hit_right_wall = False
        self.last_hit_left_wall = False
        self.ball_rect = None
        self.random_number_for_random_direction = random.randint(1,2)
        self.game_over = False
        self.random_speed = random.randint(6, 7)
        
    def draw_ball(self,screen):
        pygame.draw.circle(screen, self.ball_color, self.ball_pos, self.ball_radius * 2)
        
    def create_ball_rect(self):
        enlarged_radius = self.ball_radius + 5
        self.ball_rect = pygame.Rect(self.ball_pos.x - enlarged_radius, self.ball_pos.y - enlarged_radius, enlarged_radius * 2, enlarged_radius * 2)
        return self.ball_rect
        
    def ball_start_position(self, paddle: PaddleRect):
        self.ball_start_pos = paddle.middle_of_paddle
        return self.ball_start_pos
    
    def move_ball(self):
        self.ball_pos[0] += self.ball_speed[0]
        self.ball_pos[1] += self.ball_speed[1]

     
    def ball_hit_left_side_paddle(self, paddle: PaddleRect):
        """Checks if ball hits the left side of the paddle and if it is between boundaries"""
        y_tolerance = 7
        mid_paddle_pos = paddle.paddle_pos.x + (paddle.paddle_width / 2)
        middle_of_left_edge_paddle = (paddle.paddle_pos.x + mid_paddle_pos) / 2
        # Checks if ball is within the limits of left side of the paddle and changes speed if hit outside or inside of the left side of the paddle.
        if (paddle.paddle_pos.x <= self.ball_pos.x <= mid_paddle_pos and paddle.paddle_pos.y - y_tolerance <= self.ball_pos.y <= paddle.paddle_pos.y + y_tolerance):
            if self.ball_pos.x > middle_of_left_edge_paddle:
                self.move_ball_left()
            else:
                self.change_speed_ball_left()

    def ball_hit_right_side_paddle(self, paddle: PaddleRect):
        """Checks if ball hits the right side of the paddle and if it is between boundaries"""
        y_tolerance = 7
        mid_paddle_pos = paddle.paddle_pos.x + (paddle.paddle_width / 2)
        right_edge_paddle = mid_paddle_pos + (paddle.paddle_width / 2)
        middle_of_right_edge_paddle = (mid_paddle_pos + right_edge_paddle) / 2
        # Checks if ball is within the limits of right side of the paddle and changes speed if hit outside or inside of the right side of the paddle.
        if (mid_paddle_pos <= self.ball_pos.x <= right_edge_paddle and paddle.paddle_pos.y - y_tolerance <= self.ball_pos.y <= paddle.paddle_pos.y + y_tolerance):
            if self.ball_pos.x < middle_of_right_edge_paddle:
                self.move_ball_right()
            else:
                self.change_speed_ball_right()

    def check_if_ball_hit_paddle(self, paddle: PaddleRect):
        self.ball_hit_left_side_paddle(paddle)
        self.ball_hit_right_side_paddle(paddle)
            
    def check_if_ball_hit_top_bottom_walls(self):
        top = 0
        bottom = 720
        if self.ball_pos.y < top:
            self.ball_speed[1] *= -1
        elif self.ball_pos.y > bottom:
            self.game_over = True
  
    def check_if_ball_hit_side_walls(self):
        left_wall = 0
        right_wall = 1280
        if self.ball_pos.x < left_wall:
            self.ball_speed[0] *= -1
        elif self.ball_pos.x > right_wall:
            self.ball_speed[0] *= -1
            
    
    def move_ball_left(self):
        if self.ball_speed[0] < 0: 
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= 1       
        else:
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= -1
            

    def move_ball_right(self):
        if self.ball_speed[0] > 0: 
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= 1
        else:
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= -1
            
    def change_speed_ball_left(self):
        if self.ball_speed[0] < 0: 
            self.ball_speed[1] *= -1
            self.ball_speed[0] = -self.random_speed  
        else:
            self.ball_speed[1] *= -1
            self.ball_speed[0] = -self.random_speed
    
    def change_speed_ball_right(self):
        if self.ball_speed[0] > 0: 
            self.ball_speed[1] *= -1
            self.ball_speed[0] = self.random_speed
        else:
            self.ball_speed[1] *= -1
            self.ball_speed[0] = self.random_speed * 1
