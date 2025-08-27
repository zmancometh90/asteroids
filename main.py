import sys

import pygame
from asteroid import  *
from asteroidfield import AsteroidField
from bullet import Shot
from constants import *
from player import Player


def main():
    pygame.init()
    startMessage = "Press any key to start"
    endMessage = "GAME OVER!"
    font = pygame.font.SysFont("Arial", 60)
    text_surface = font.render(endMessage, True, "white")
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()


    player = Player(
        x=SCREEN_WIDTH / 2,
        y=SCREEN_HEIGHT / 2,
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collides_with(asteroid):
                    asteroid.split()
                    bullet.kill()
            if player.collides_with(asteroid):
                screen.blit(text_surface, text_rect)
                pygame.display.flip()
                pygame.time.wait(2000)
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # render the background
        pygame.display.flip()

        # wait wait 60 frames and redraw
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
