import pygame
import random
import time,os

pygame.init()

class Pear(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))


pygame.display.set_mode((800,500))
pygame.display.set_caption('Tag it!')
pygame.display.set_icon(pygame.image.load("images/icon.bmp"))

def update():
    x=random.randint(50, 750)
    y=random.randint(50, 450)

screen = pygame.display.set_mode((800, 500))

bg = pygame.image.load('images/bg.png')
score = 0


speed = 1
b1 = Pear(1000//2, "images/pear3.png")
 
f2 = pygame.font.SysFont('Akshar', 48)
text2 = f2.render(f'Score: {score}', True,
                  ('white'))

x1=random.randint(50, 750)
y1=random.randint(50, 450)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  
        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(x,y)
                os.system('cls')
                if (x in range(0,50)) and (y in range(0,50)):
                    print('курсор в регионе')
                    time.sleep(0.5)
        


         

    screen.blit(bg, (0, 0))
    screen.blit(b1.image, (x1, y1))
    screen.blit(text2, (10, 10))
    pygame.display.update()