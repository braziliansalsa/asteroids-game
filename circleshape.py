import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite): # This is a base class for circular shapes in the game
    def __init__(self, x, y, radius): # Initialize the CircleShape with position and radius
        # we will be using this later
        if hasattr(self, "containers"): # Check if the class has a containers attribute
            super().__init__(self.containers) # If it does, initialize the sprite with the containers
        else:
            super().__init__() # Otherwise, just initialize the sprite without containers

        self.position = pygame.Vector2(x, y) # Set the position of the circle shape
        self.velocity = pygame.Vector2(0, 0) # Initialize velocity to zero
        self.radius = radius # Set the radius of the circle shape

    def draw(self, screen): # Draw the circle shape on the screen
        pass
    def update(self, dt): # Update the circle shape's position based on its velocity and delta time 
        pass