from types import new_class

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random.uniform(20, 50)
        rotated_vector_1 = self.velocity.rotate(random.uniform(0, 360))
        rotated_vector_2 = self.velocity.rotate(random.uniform(0, -360))

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = rotated_vector_1 * 1.2
        asteroid2.velocity = rotated_vector_2 * 1.2
