# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize Pygame
    pygame.init()
    pygame.time.Clock() # Create a clock to manage frame rate
    dt = 0.0 # Initialize delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:

        for event in pygame.event.get(): # Check for events
            if event.type == pygame.QUIT: # If the quit event is triggered
                return # Exit the game loop
        screen.fill((0, 0, 0)) # Fill the screen with black
        pygame.display.flip() # Update the display
        pygame.time.Clock().tick(60) # Limit the frame rate to 60 FPS
        dt = pygame.time.Clock().tick(60) / 1000.0
        print(f"Delta time: {dt:.3f} seconds")


if __name__ == "__main__":
    main()