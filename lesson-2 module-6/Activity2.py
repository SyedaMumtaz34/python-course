import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,0,0))
WHITE=(255,255,255)
pygame.draw.circle(screen,WHITE,(300,300),50)
pygame.draw.circle(screen,WHITE,(100,100),50,3)
pygame.display.update()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
pygame.quit()