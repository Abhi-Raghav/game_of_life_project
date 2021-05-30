# Simple pygame program

# Import pygame and initialize it
import pygame
# This function calls the separate init() functions of all the included pygame modules. Since these modules are
# abstractions for specific hardware, this initialization step is required so that you can work with the same code on
# Linux, Windows, and Mac.
pygame.init()


# In pygame, everything is viewed on a single user-created display, which can be a window or a full screen. The
# display is created using .set_mode(), which returns a Surface representing the visible part of the window. It is
# this Surface that you pass into drawing functions like pygame.draw.circle(), and the contents of that Surface are
# pushed to the display when you call pygame.display.flip(). Setup the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background in white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle at the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit
pygame.quit()
