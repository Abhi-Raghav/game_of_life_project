# basic game design
import pygame
import random

# Import pygame.locals for easier access to coordinates
# Updated to conform to flak8 and black standard
from pygame.locals import (
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT,
)

# Initialize pygame
pygame.init()

# Defining constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Next, you write a method in Player to accepts that dictionary. This will define the behavior of the sprite
    # based off the keys that are pressed.
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    # K_UP, K_DOWN, K_LEFT, and K_RIGHT correspond to the arrow keys on the keyboard. If the dictionary entry for
    # that key is True, then that key is down, and you move the player .rect in the proper direction. Here you use
    # .move_ip(), which stands for move in place, to move the current Rect.

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        # you update rect to be a random location along the right edge of the screen. The center of the rectangle is
        # just off the screen. It’s located at some position between 20 and 100 pixels away from the right edge,
        # and somewhere between the top and bottom edges.
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# This returns a Surface which represents the inside dimensions of the window. This is the portion of the window you
# can control, while the OS controls the window borders and title bar.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
# pygame defines events internally as integers, so you need to define a new event with a unique integer. The last
# event pygame reserves is called USEREVENT, so defining ADDENEMY = pygame.USEREVENT + 1 on line 83 ensures it’s
# unique.
#
# Next, you need to insert this new event into the event queue at regular intervals throughout the game. That’s where
# the time module comes in. Line 84 fires the new ADDENEMY event every 250 milliseconds, or four times per second.
# You call .set_timer() outside the game loop since you only need one timer, but it will fire throughout the entire
# game.


# Instantiate Player. Right not it is a rectangle
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# When you call .kill(), the Sprite is removed from every Group to which it belongs. This removes the references to
# the Sprite as well, which allows Python’s garbage collector to reclaim the memory as necessary.

# You access the list of all active events in the queue by calling pygame.event.get().
# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the escape key? If yes stop the loop
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button?
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # pygame also provides pygame.event.get_pressed(), which returns a dictionary containing all the current KEYDOWN
    # events in the queue.
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on keypress
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()


    # Fill the screen with white
    # screen.fill((255, 255, 255))
    screen.fill((0, 0, 0))


    # Create a surface and pass a tuple with its length and width
    # surf = pygame.Surface((50, 50))

    # Give the surface a color to separate from the background
    # surf.fill((0, 0, 0))
    # rect = surf.get_rect()
    # After the screen is filled with white on line 45, a new Surface is created on line 48. This Surface is 50 pixels
    # wide, 50 pixels tall, and assigned to surf. At this point, you treat it just like the screen. So on line,
    # 51 you fill it with black. You can also access its underlying Rect using .get_rect(). This is stored as rect for
    # later use.

    # Just creating a new Surface isn’t enough to see it on the screen. To do that, you need to blit the Surface onto
    # another Surface. The term blit stands for Block Transfer, and .blit() is how you copy the contents of one
    # Surface to another. You can only .blit() from one Surface to another, but since the screen is just another
    # Surface, that’s not a problem. Here’s how you draw surf on the screen:

    # This line says "Draw the surface at the center of the screen"
    # screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # pygame.display.flip()

    # The .blit() call on line 55 takes two arguments:
    #
    # The Surface to draw The location at which to draw it on the source Surface The coordinates (SCREEN_WIDTH/2,
    # SCREEN_HEIGHT/2) tell your program to place surf in the exact center of the screen, but it doesn’t quite look
    # that way:

    # Put the center of surf at the center of display
    # surf_center = (
    #    (SCREEN_WIDTH - surf.get_width())/2,
    #    (SCREEN_HEIGHT - surf.get_height())/2
    # )

    # Draw the player on the screen
    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # screen.blit(player.surf, player.rect)   # When you pass a Rect to .blit(), it uses the coordinates of the top left
    # corner to draw the surface. You’ll use this later to make your player move!

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    # call to pygame.display.flip() after the call to blit(). This updates the entire screen with everything that’s
    # been drawn since the last flip. Without the call to .flip(), nothing is shown.








