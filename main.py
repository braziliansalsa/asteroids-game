import pygame
from constants import *
from player import Player

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # Create a clock to manage frame rate
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    player = Player(x, y)        # insantiate the player object
    dt = 0.0 # Initialize delta time

    while True:

        for event in pygame.event.get(): # Check for events
            if event.type == pygame.QUIT: # If the quit event is triggered
                return # Exit the game loop
        
        player.update(dt)
        
        screen.fill((0, 0, 0)) # Fill the screen with black
        player.draw(screen) # Draw the player on the screen
        pygame.display.flip() # Update the display
        
        # limits the frame rate to 60 FPS
        dt = pygame.time.Clock().tick(60) / 1000.0

if __name__ == "__main__":
    main()