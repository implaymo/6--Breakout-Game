# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(100,700)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    player_pos_tuple = (int(player_pos.x), int(player_pos.y))
    pygame.draw.rect(screen, "black", pygame.Rect(player_pos_tuple[0], player_pos_tuple[1], 200, 10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 1000 * dt
    if keys[pygame.K_d]:
        player_pos.x += 1000 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()