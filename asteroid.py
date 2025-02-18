from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius = self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        old_radius = self.radius
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(rand_angle)
        vector_2 = self.velocity.rotate(-rand_angle)
        new_asteroid_rad = old_radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_rad)
        asteroid_1.velocity += vector_1 * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_rad)
        asteroid_2.velocity += vector_2 * 1.2
