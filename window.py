import pygame
from paddle import PaddleRect
from blocks import Block
from ball import GameBall

class Screen:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.paddle = PaddleRect()
        self.block = Block()
        self.game_ball = GameBall(self.paddle)



    def run_game(self): 
        
        pygame.init()
        pygame.display.set_caption("My Breakout Game")
            
        
                    
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("black")
            
            
            # Create objects
            self.block.draw_multiple_blocks(self.screen)
            self.paddle.draw_paddle(self.screen)
            self.game_ball.draw_ball(self.screen)
            self.game_ball.create_ball_rect()
            
            self.game_ball.random_direction(self.paddle)

            
            self.game_ball.move_ball()
            
            # Check collisions
            self.block.check_collision_with_ball(self.game_ball)
            self.game_ball.check_if_ball_hit_paddle(self.paddle) 
            self.game_ball.check_if_ball_hit_top_bottom_edges() 
            self.game_ball.check_if_ball_hit_side_edges()  
            
            self.paddle.move_player(self.dt)

            
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
            
    
        
    def end_game(self):
        pygame.quit()
        
        

        