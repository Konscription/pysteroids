# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(window, (0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()