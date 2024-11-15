import pygame
import random


GRID_WIDTH = 32
GRID_HEIGHT = 32
GRID_COLUMNS = 20
GRID_ROWS = 16
WINDOW_WIDTH = GRID_WIDTH * GRID_COLUMNS
WINDOW_HEIGHT = GRID_HEIGHT * GRID_ROWS


BACKGROUND_COLOR = (144, 238, 144)
GRID_COLOR = (0, 0, 0)

def draw_grid(screen):
    """Draws a 20x16 grid on the screen."""
    for x in range(0, WINDOW_WIDTH, GRID_WIDTH):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_HEIGHT):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

def draw_mole(screen, mole_image, mole_pos):
    """Draw the mole image at the given position (mole_pos)."""
    screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos[0] * GRID_WIDTH, mole_pos[1] * GRID_HEIGHT)))

def handle_click(event, mole_pos):
    """Move the mole to a random position when clicked."""
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos

        clicked_column = mouse_x // GRID_WIDTH
        clicked_row = mouse_y // GRID_HEIGHT


        if (clicked_column, clicked_row) == mole_pos:
            mole_pos = (random.randint(0, GRID_COLUMNS - 1), random.randint(0, GRID_ROWS - 1))
    return mole_pos

def main():
    pygame.init()


    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Whack-a-Mole")


    mole_image = pygame.image.load("mole.png")


    mole_pos = (random.randint(0, GRID_COLUMNS - 1), random.randint(0, GRID_ROWS - 1))


    clock = pygame.time.Clock()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            mole_pos = handle_click(event, mole_pos)


        screen.fill(BACKGROUND_COLOR)


        draw_grid(screen)


        draw_mole(screen, mole_image, mole_pos)


        pygame.display.flip()

        
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

