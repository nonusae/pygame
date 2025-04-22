import pygame
from player import *
from constants import *
from asteroid import Asteroid
from asteroidfield import *

def main():

    pygame.init()# Setup display and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    Player.containers = updatable, drawable
    Asteroid.containers = asteriods, updatable, drawable
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for member in drawable:
            member.draw(screen)

        pygame.display.flip()

        t = clock.tick(60)
        dt = t / 1000

if __name__ == "__main__":
    main()
