import pygame
from paddle import PaddleRect
from blocks import Block
from ball import GameBall
from score import NewScore
from level import NewLevel

class Screen:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.paddle = PaddleRect()
        self.block = Block()
        self.game_ball = GameBall(self.paddle)
        self.new_score = NewScore()
        self.new_level = NewLevel()
        self.game_started = False
        self.player_won = False
    

    def run_game(self): 
        
        pygame.init()
        pygame.display.set_caption("My Breakout Game")
  
        self.block.create_all_block_rects()
        
                    
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  
                        self.game_started = True
            self.screen.fill("black")
            
        
            
            # Score and Highscore text
            score_text = self.new_score.render_score(self.block)
            self.screen.blit(score_text, (10, 10))

            highscore_text = self.new_score.render_highscore() 
            self.screen.blit(highscore_text, (10, 40))  
            self.new_score.high_score(self.block, self.game_ball)

            level_text = self.new_level.render_level()
            self.screen.blit(level_text, (640, 10))

            # Create objects
            self.block.draw_multiple_blocks(self.screen)
            self.paddle.draw_paddle(self.screen)
            self.game_ball.draw_ball(self.screen)
            self.game_ball.create_ball_rect()
            self.game_ball.ball_start_position(self.paddle)

            

            if self.game_started:
                self.start_game()
                
                
            if self.game_ball.game_over is True:   
                self.new_score.high_score(self.block, self.game_ball) 
                self.restart_game()
            else:
                self.restart_game_if_user_wins()
                


            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
        
    def end_game(self):
        pygame.quit()
        
    def start_game(self):
        self.game_ball.move_ball()
        # Check collisions
        self.block.check_collision_with_ball(self.game_ball)
        self.game_ball.check_if_ball_hit_paddle(self.paddle) 
        self.game_ball.check_if_ball_hit_top_bottom_walls() 
        self.game_ball.check_if_ball_hit_side_walls()  
        
        self.paddle.move_player(self.dt)
    
    def restart_game(self):
        bottom = 720
        if self.game_ball.ball_pos.y > bottom:
            self.new_level.reset_level()
            self.paddle = PaddleRect()
            self.game_ball = GameBall(self.paddle)
            self.block = Block()
            self.block.create_all_block_rects()
            self.block.reset_block_counting()
            self.game_started = False
    
    def restart_game_if_user_wins(self):
        bottom = 720
        if not self.block.all_blocks:
            self.player_won = True
            
        if self.game_ball.ball_pos.y < bottom and self.player_won is True:
            self.new_level.change_level()
            self.paddle.change_paddle_size()
            self.game_ball = GameBall(self.paddle)
            self.block.create_all_block_rects()
            self.game_started = False
            self.player_won = False

            
            
            