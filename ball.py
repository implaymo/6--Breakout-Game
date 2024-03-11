import pygame
from paddle import PaddleRect

class GameBall:
    def __init__(self) -> None:
        self.ball_pos = pygame.Vector2(640, 690)
        self.ball_color = "white"
        self.ball_speed = [0.5, 3]
        
        
        
    def draw_ball(self,screen):
        pygame.draw.circle(screen, self.ball_color, self.ball_pos, 10)
        
    def move_ball(self):
        self.ball_pos.y -= self.ball_speed[1]
        self.ball_pos.x += self.ball_speed[0]

    def ball_hit_left_side_paddle(self, paddle: PaddleRect):
        """Checks if ball hits the left side of the paddle and if it is between boundaries"""
        y_tolerance = 5
        if (self.ball_pos.x <= paddle.paddle_pos.x + (paddle.paddle_width / 2) and paddle.paddle_pos.y - y_tolerance <= self.ball_pos.y <= paddle.paddle_pos.y + y_tolerance):
            self.move_ball_diagonal_left_up()
            print(f"PADDLE X POSITION {paddle.paddle_pos.x} ")
            print(f"BALL X POSITION = {self.ball_pos.x}")
    

    def ball_hit_right_side_paddle(self, paddle: PaddleRect):
        """Checks if ball hits the right side of the paddle and if it is between boundaries"""
        y_tolerance = 5
        if (self.ball_pos.x >= paddle.paddle_pos.x + (paddle.paddle_width / 2) and paddle.paddle_pos.y - y_tolerance <= self.ball_pos.y <= paddle.paddle_pos.y + y_tolerance):
            
            self.move_ball_diagonal_right_up()
            print(f"PADDLE X POSITION {paddle.paddle_pos.x} ")
            print(f"BALL X POSITION = {self.ball_pos.x}")
            
    def check_if_ball_hit_paddle(self, paddle: PaddleRect):
        self.ball_hit_left_side_paddle(paddle)
        self.ball_hit_right_side_paddle(paddle)
            
    
    def check_if_ball_hit_top_bottom_edges(self):
        if self.ball_pos.y < 0:
            self.ball_speed[1] *= -1
            self.ball_speed[0] *= 1
        elif self.ball_pos.y > 720:
            print("Game Over")
            self.ball_pos.y = 600
            
    def check_if_ball_hit_sides_edges(self):
        pass

    def move_ball_diagonal_left_up(self):
        print("HIT LEFT PADDLE")
        self.ball_speed[1] *= -1
        self.ball_speed[0] *= -1

    def move_ball_diagonal_right_up(self):
        print("HIT RIGHT PADDLE")
        self.ball_speed[1] *= -1
        self.ball_speed[0] *= -1


  
            