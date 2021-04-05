import pygame
import math
pygame.init()
size = width, height = (1000, 700)
black = (0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
blue = (0,0, 255)
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.display.set_caption("tsis")

#рама
pygame.draw.rect(screen, black, (50, 50, width-100, height-100), 2)
pygame.draw.line(screen,black,(50,75),(width - 50 , 75),2 )
font = pygame.font.Font(None, 20)
text1 = font.render("1.00",False,black )
screen.blit(text1, ( 20, 70))
pygame.draw.line(screen,black,(50,height-75),(width - 50 , height -75),2 )
pygame.draw.line(screen, black,(75, 50),(75, height -50), 2)
pygame.draw.line(screen, black,(width -75, 50),(width-75, height -50), 2)
#3Pi
h = 75
e =-3
while h <= width-75:
    font = pygame.font.Font(None, 25)
    pi3 = font.render(str(e)+"п",False,black )
    screen.blit(pi3, ( h, height -45))
    h = h+70
    e = e +0.5
#big plus
pygame.draw.line(screen, black, (50, height/2), (width-50, height/2), 2)
pygame.draw.line(screen, black, (width/2, 50), (width/2, height-50), 2)
#numbers 
q = -3
i = 75
while q <0:
    font = pygame.font.Font(None, 25)
    n = font.render(str(q),False,black )
    screen.blit(n, ( i+5, height/2+60))
    q= q +1
    i= i+140
#sin cosx ----
font = pygame.font.Font(None, 30)
n = font.render("Sin x",False,black )
screen.blit(n, ( 630, 80))
pygame.draw.line(screen,red, (685, 90), (720,90), 4)
font = pygame.font.Font(None, 30)
m = font.render("Cos x",False,black )
screen.blit(m, ( 630, 100))
pygame.draw.line(screen,blue, (687, 110), (720,110), 4)

y = 100
#маленькие
while y< 900:
    pygame.draw.line(screen, black, (y, 50),( y, 60), 2)
    pygame.draw.line(screen, black, (y, height-50),( y, height-60), 2)
    y = y+20
    if y%40==0:
        pygame.draw.line(screen, black, (y, 50),( y, 65), 2)
        pygame.draw.line(screen, black, (y, height-50),( y, height-65), 2)
t = 75
while t < height -100:
    pygame.draw.line(screen, black, (50, t), (60, t))
    pygame.draw.line(screen, black, (950, t), (940, t))
    t = t + 15
    if t%30==0:
        pygame.draw.line(screen, black, (50, t), (65, t))
        pygame.draw.line(screen, black, (950, t), (935, t))
    
k = 50
l= 0.25
s = 0.75
#горизонтальные 
while k < 600 :  
    if s== -1.0:
        font = pygame.font.Font(None, 20)
        text = font.render("-1.00",False,black )
        screen.blit(text, ( 20, height-80))     
        break
    pygame.draw.line(screen, black, (50, k),(width -50, k),2)
    k = k+75
    font = pygame.font.Font(None, 20)
    text = font.render(str('%.2f'%s),False,black )
    screen.blit(text, ( 20, k-5))
    s = s-l

        
j= 50
#вертикальные 
while j<width:
    if j ==650:
        pygame.draw.line(screen, black,(j, 125), (j, height - 50), 2)
    else:
        pygame.draw.line(screen, black,(j, 50), (j, height - 50), 2)
    j = j +150
x = 75
dx = 4
def f_cos(x, d):
    return -1*math.cos((x-width/2)/45)*d+height/2
def f_sin(x, d):
    return -1*math.sin((x-width/2)/45)*d+height/2
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if x<width-50:
        if x%5==0:
            pygame.draw.line(screen, white, (x, f_cos(x,273)), (x+dx, f_cos(x+dx, 273)), 2)
        else:
            pygame.draw.line(screen, blue, (x, f_cos(x,273)), (x+dx, f_cos(x+dx, 273)), 2)
        pygame.draw.line(screen, red, (x, f_sin(x,273)), (x+dx, f_sin(x+dx, 273)), 2)

    x+=dx
    pygame.display.flip()

pygame.quit()