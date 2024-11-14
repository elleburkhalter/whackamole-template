import pygame
import random

def draw_grid(screen):
    for x in range(0, 640, 32):
        pygame.draw.line(screen, 'black', (x,0), (x, 512))
    for y in range(0, 512, 32):
        pygame.draw.line(screen, 'black', (0, y), (640, y))

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        position = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_x,mole_y = position
                    if mole_x <= mouse_x < mole_x + 32 and mole_y <= mouse_y < mole_y + 32:
                        position = (random.randrange(0, 20) * 32, random.randrange(0, 16) * 32)
            screen.fill("pink")
            draw_grid(screen)
            screen.blit(mole_image, position)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
