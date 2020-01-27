import pygame
import random
pygame.init()

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("SNAKES WITH DASSANI")
pygame.display.update()

exit_game=False
game_over=False
snake_x=45
snake_y=55
v_x=0
v_y=0

food_x=random.randint(0,screen_width)
food_y=random.randint(0,screen_height)
score=0
snake_size=10
fps=30

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def draw_snake(snake_x,snake_y):
    snake=[]
    
    

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                v_x=5
                v_y=0

            if event.key==pygame.K_LEFT:
                v_x=-5
                v_y=0

            if event.key==pygame.K_UP:
                v_y=-5
                v_x=0

            if event.key==pygame.K_DOWN:
                v_y=5
                v_x=0

    snake_x+=v_x
    snake_y+=v_y
    if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
        score+=1
        food_x=random.randint(0,screen_width)
        food_y=random.randint(0,screen_height)

    gameWindow.fill(white)
    text_screen("Sccore: "+ str(score*10), red, 5, 5)
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow,red,[food_x,food_y,10,10])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()