import pygame
import random
pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

score=0
screen=pygame.display.set_mode((WIDTH,HEIGHT))
myfont=pygame.font.Font(None,30)

def random_apple():
    while True:
        position=random.randrange(0,(WIDTH//CELL_SIZE))*CELL_SIZE, random.randrange(0,(HEIGHT//CELL_SIZE))*CELL_SIZE
        if position not in snake:
            return position
        
snake=[(100,100)]
direction=(CELL_SIZE,0)
speed=10
apple_pos=random_apple()


running=True
clock=pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and direction!=(0,CELL_SIZE):
                direction=(0,-CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    new_head=(snake[0][0]+direction[0],snake[0][1]+direction[1])

    if new_head in snake or not (0<=new_head[0]<WIDTH and 0<=new_head[1]<HEIGHT):
        running = False
    snake.insert(0,new_head)
    if new_head==apple_pos:
        score+=1
        if score%5==0:
            speed+=2
        apple_pos=random_apple()
    else:
        snake.pop()

    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(screen,GREEN,(*segment,CELL_SIZE,CELL_SIZE))

    pygame.draw.rect(screen, RED, (*apple_pos, CELL_SIZE, CELL_SIZE))
    score_text = myfont.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (50, 50)) 
    pygame.display.flip()
    clock.tick(speed)