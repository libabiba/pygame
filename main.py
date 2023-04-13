

import pygame
 
class Pear(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

class ClickableSprite(pygame.sprite.Sprite):

    def __init__(self, image, x, y, callback):

        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.callback = callback
 

    def update(self, events):

        for event in events:

            if event.type == pygame.MOUSEBUTTONUP:

                if self.rect.collidepoint(event.pos):

                    self.callback()
 
 

def on_click():

    color = (255, 0, 0) if sprite.image.get_at(

        (0, 0)) != (255, 0, 0) else (0, 255, 0)

    sprite.image.fill(color)
 
 
pygame.init()

score=1
pygame.display.set_mode((800,500))
pygame.display.set_caption('Tag it!')
pygame.display.set_icon(pygame.image.load("images/icon.bmp"))
 
f2 = pygame.font.SysFont('Akshar', 48)
text2 = f2.render(f'Score: {score}', True,
                  ('white'))

speed = 1
b1 = Pear(1000//2, "images/pear3.png")

bg = pygame.image.load('images/bg.png')

screen = pygame.display.set_mode((800, 500))

sprite = ClickableSprite(pygame.Surface((100, 100)), 50, 50, on_click)

group = pygame.sprite.GroupSingle(sprite)
 

running = True

while running:

    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:

            running = False
 

    group.update(events)



    screen.blit(bg, (0, 0))
    screen.blit(b1.image, (50, 50))
    screen.blit(text2, (10, 10))
    pygame.display.update()
 
pygame.quit()