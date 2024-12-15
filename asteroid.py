import pygame
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_SPLIT_SPEED_SCALING_FACTOR
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20.0, 50.0)
        first_half_velocity = self.velocity.rotate(split_angle)
        second_half_velocity = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_half_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        first_half_asteroid.velocity = first_half_velocity * ASTEROID_SPLIT_SPEED_SCALING_FACTOR
        second_half_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_half_asteroid.velocity = second_half_velocity * ASTEROID_SPLIT_SPEED_SCALING_FACTOR