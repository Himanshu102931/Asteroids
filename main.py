from asteroidfield import AsteroidField
from asteroid import Asteroid
import pygame
from constants import  SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from circleshape import CircleShape
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    hero = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)



    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(hero):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()


        screen.fill(color="Black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/ 1000



if __name__ == "__main__":
    main()
