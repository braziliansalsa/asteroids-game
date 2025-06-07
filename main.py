import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    pygame.display.set_caption("Asteroids") # Set the window title
    
    updatable = pygame.sprite.Group() # Createddddd a group for updatable objects
    drawable = pygame.sprite.Group() # Create a group for drawable objects
    asteroids = pygame.sprite.Group() # Create a group for asteroids
    shots = pygame.sprite.Group() # Create a group for shots

    Player.containers = (updatable, drawable) # Assign the player to both groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)        # insantiate the player object
    asteroid_field  = AsteroidField()

    dt = 0.0 # Initialize delta time

    while True:

        for event in pygame.event.get(): # Check for events
            if event.type == pygame.QUIT: # If the quit event is triggered
                return # Exit the game loop
        
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    print("Asteroid destroyed!")
                    shot.kill()
                    asteroid.split() 
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()

        screen.fill((0, 0, 0)) # Fill the screen with black
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip() # Update the display
        
        # limits the frame rate to 60 FPS
        dt = pygame.time.Clock().tick(60) / 1000.0

if __name__ == "__main__":
    main()