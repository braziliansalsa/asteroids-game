import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)  # Initialize the CircleShape with position and radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt  # Update position based on velocity and delta time

    