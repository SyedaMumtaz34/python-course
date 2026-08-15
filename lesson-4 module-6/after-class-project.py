import pygame
import random

pygame.init()

# Screen settings
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")

# Game settings
SPEED = 5
FONT_SIZE = 36

# Load and scale background
background = pygame.image.load("pet_bg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Named font
font = pygame.font.SysFont("Arial", FONT_SIZE)

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size):
        super().__init__()

        self.image = pygame.Surface((size, size))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Pet class
class Pet(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 150, 150), 50)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # Keep pet inside screen
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))


# Food class
class Food(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 220, 50), 30)


# Create pet and food
pet = Pet(50, 170)
pet_food = Food(350, 200)

# Sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(pet)
all_sprites.add(pet_food)

food_collected = False

# Clock
clock = pygame.time.Clock()

# Game loop
running = True

while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard movement
    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if keys[pygame.K_LEFT]:
        dx = -SPEED
    if keys[pygame.K_RIGHT]:
        dx = SPEED
    if keys[pygame.K_UP]:
        dy = -SPEED
    if keys[pygame.K_DOWN]:
        dy = SPEED

    pet.move(dx, dy)

    # Collision detection
    if not food_collected:
        if pet.rect.colliderect(pet_food.rect):
            all_sprites.remove(pet_food)
            food_collected = True

    # Draw background
    screen.blit(background, (0, 0))

    # Draw sprites
    all_sprites.draw(screen)

    # Display completion message
    if food_collected:
        message = font.render("Food Collected!", True, (255, 255, 255))

        x = (WIDTH - message.get_width()) // 2
        y = (HEIGHT - message.get_height()) // 2

        screen.blit(message, (x, y))

    # Update screen
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()