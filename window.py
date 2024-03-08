import pygame
from paddle import PaddleRect

class Screen():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.paddle = PaddleRect()
        
        
    def run_game(self): 
        pygame.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("purple")
            
            self.paddle.draw(self.screen)
            self.paddle.move_player(self.dt)
            
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
            
    
        
    def end_game(self):
        pygame.quit()