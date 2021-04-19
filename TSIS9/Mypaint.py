import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Paint')
clock = pygame.time.Clock()

game_over = False
prev, cur = None, None
screen.fill(WHITE)

#colors
pygame.draw.circle(screen, RED, (25,25), 15)
pygame.draw.circle(screen, GREEN, (60,25), 15)
pygame.draw.circle(screen, BLUE, (95,25), 15)
pygame.draw.circle(screen, BLACK, (130,25), 15)
color = []
color.append(BLACK)

myfont = pygame.font.SysFont('Comic Sans MS',20 )
textsurface = myfont.render('Palette', True, (130,170,204))
screen.blit(textsurface,(10,40)) 

#figures
pygame.draw.circle(screen, (155,155,155), (250,25), 15)
pygame.draw.rect(screen, (155,155,155),(285,10,30 , 30), 5)
pygame.draw.line(screen, (155,155,155),(335, 25), (375,25) ,15 )

myfont = pygame.font.SysFont('Comic Sans MS',20 )
textsurface = myfont.render('Draw under the line', True, (130,170,204))
screen.blit(textsurface,(150,50))

pygame.draw.line(screen, BLACK,(0, 80), (500,80) ,5)
#eraser
pygame.draw.rect(screen, BLACK,(400,10,30 , 30), 5)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS',15 )
textsurface = myfont.render('eraser', True, (130,170,204))
screen.blit(textsurface,(400,35))
figure = []
figure.append("line")
figure.append("line")
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.image.save(screen, 'save.jpg')
      game_over = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if x  in range(400,430) and y in range(10,40):
            figure.append("eraser")
            break                
        if x  in range(335,375) and y in range(10,40):
            figure.append("line")
            break        
        if x  in range(235,265) and y in range(10,40):
            figure.append("circle")
            break
        if x  in range(285,315) and y in range(10,40):
            figure.append("rect")
            break
        if x  in range(10,40) and y in range(10,40):
            color.append(RED)
            break
        if x  in range(45,75) and y in range(10,40):
            color.append(GREEN)
            break
        if x  in range(80,110) and y in range(10,40):
            color.append(BLUE)
            break    
        if x  in range(115,145) and y in range(10,40):
            color.append(BLACK)
            break
    
    if figure[len(figure)-1] == "line":
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if prev:
            pygame.draw.line(screen, color[len(color)-1], prev, cur, 2)
            prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None

#circle
    if figure[len(figure)-1] == "circle":
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cur = pygame.mouse.get_pos()
        if prev:
            pygame.draw.circle(screen, color[len(color)-1], prev,15)
            prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None

#rect
    if figure[len(figure)-1] == "rect":
        if event.type == pygame.MOUSEBUTTONDOWN:
            a, b = pygame.mouse.get_pos()
        
            pygame.draw.rect(screen, color[len(color)-1], (a,b ,25, 25), 5)
            

#eraser
    if figure[len(figure)-1] == "eraser":
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if prev:
            pygame.draw.line(screen, WHITE, prev, cur, 10)
            prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
  # if prev:
  #   pygame.draw.circle(screen, RED, prev, 10)

  pygame.display.flip()

  clock.tick(30)


pygame.quit()
