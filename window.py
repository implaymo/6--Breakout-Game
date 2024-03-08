import pygame

class Screen():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        
        
    def run_game(self): 
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("purple")
            
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
            
    
        
    def end_game(self):
        pygame.quit()