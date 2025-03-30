import pygame
import random, time

clock = pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((400,600))
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
speed = 5
bg=pygame.image.load('images/AnimatedStreet.png')
bg_y=0
running=True
myfont=pygame.font.Font(None,40)
game_over=myfont.render('Game over',True,BLACK)
class Enemy(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("images/Enemy.png")
            self.rect=self.image.get_rect()
            self.rect.center=(random.randint(40,360),0)

        def move(self):
            self.rect.move_ip(0,speed)
            if self.rect.bottom>600:
                self.rect.top=0
                self.rect.center=(random.randint(30,370),0)

        def draw(self,surface):
            surface.blit(self.image,self.rect)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("images/Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=(200,550)

    def move(self):
        keys=pygame.key.get_pressed()
        if self.rect.left>0:
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 400:        
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
                  
    def draw(self,surface):
        surface.blit(self.image,self.rect)

P1=Player()
E1=Enemy()

enemies=pygame.sprite.Group()
enemies.add(E1)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

inc_speed=pygame.USEREVENT+1
pygame.time.set_timer(inc_speed, 1000)

while running:
    screen.blit(bg,(0, bg_y))
    screen.blit(bg,(0, bg_y - 600))

    for event in pygame.event.get():
        if event.type==inc_speed:
            speed+=0.5
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()

    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("images/crash.wav").play()
        screen.fill(RED)
        screen.blit(game_over,(200,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(4)
        running=False
        pygame.quit() 
    if bg_y==600:
        bg_y=0
    else:
        bg_y+=5

    P1.move()
    E1.move()

    P1.draw(screen)
    E1.draw(screen) 

    pygame.display.update()

    clock.tick(60)        