import pygame
import random

# Constants for grid size and window size
GRID_WIDTH = 32
GRID_HEIGHT = 32
GRID_COLUMNS = 20
GRID_ROWS = 16
WINDOW_WIDTH = GRID_WIDTH * GRID_COLUMNS
WINDOW_HEIGHT = GRID_HEIGHT * GRID_ROWS

# Colors
BACKGROUND_COLOR = (144, 238, 144)  # Light green background
GRID_COLOR = (0, 0, 0)  # Black grid lines

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
        # Convert mouse coordinates to grid coordinates
        clicked_column = mouse_x // GRID_WIDTH
        clicked_row = mouse_y // GRID_HEIGHT
        
        # If the clicked square is where the mole is, move it
        if (clicked_column, clicked_row) == mole_pos:
            mole_pos = (random.randint(0, GRID_COLUMNS-1), random.randint(0, GRID_ROWS-1))
    return mole_pos
def main():
    pygame.init()

    # Create the display window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Whack-a-Mole")

    # Load the mole image
    mole_image = pygame.image.load("mole.png")
    
    # Initial position of the mole (top-left corner)
    mole_pos = (0, 0)

    # Create the clock object to control frame rate
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check if mouse clicked the mole's square
            mole_pos = handle_click(event, mole_pos)

        # Fill the screen with background color
        screen.fill(BACKGROUND_COLOR)

        # Draw the grid
        draw_grid(screen)

        # Draw the mole in the current position
        draw_mole(screen, mole_image, mole_pos)

        # Update the screen
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
