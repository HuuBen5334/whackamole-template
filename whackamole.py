import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        color = (0,0,0)
        running = True
        x = 0
        y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if x < mouse_pos[0] < (32 + x) and y < mouse_pos[1] < (32 + y):
                        x = random.randrange(0, 20) * 32
                        y = random.randrange(0, 16) * 32
                    print(event.pos)


            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))

            for i in range(1, 20):
                pygame.draw.line(screen, color, (32 * i, 0), (32 * i, 512))
            for i in range(1, 16):
                pygame.draw.line(screen, color, (0, 32 * i), (640, 32 * i))

            pygame.display.flip()
            clock.tick(60)



    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
