import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen): # Draw the circle shape on the screen
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt): # Update the circle shape's position based on its velocity and delta time 
        self.position += self.velocity * dt