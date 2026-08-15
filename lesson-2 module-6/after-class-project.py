import pygame
pygame.init()
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Mini Sprite Adventure")
x=370
y=270
sprite_width = 60
sprite_height = 40
speed = 5
background_color = (30, 30, 60)
circle_color = (255, 200, 0)
outline_color = (0, 255, 255)

sprite_color = (0, 200, 100)
left_color = (255, 80, 80)
right_color = (80, 80, 255)
top_color = (255, 200, 50)
bottom_color = (180, 80, 255)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed
    x = max(0, min(x, screen_width - sprite_width))
    y = max(0, min(y, screen_height - sprite_height))
    if x == 0:
        sprite_color = left_color
    elif x == screen_width - sprite_width:
        sprite_color = right_color
    elif y == 0:
        sprite_color = top_color
    elif y == screen_height - sprite_height:
        sprite_color = bottom_color
    else:
        sprite_color = (0, 200, 100)
    screen.fill(background_color)
    pygame.draw.circle(screen, circle_color, (100, 100), 40)
    pygame.draw.circle(screen, outline_color, (700, 500), 50, 5)
    sprite = pygame.Rect(x, y, sprite_width, sprite_height)
    pygame.draw.rect(screen, sprite_color, sprite)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()