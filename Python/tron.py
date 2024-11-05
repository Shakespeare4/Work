import pygame
import time
import random
 
pygame.init()

 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
#tamaño del cuadrado
dis_width = 600
dis_height = 400
x1 = dis_width / 2
y1 = dis_height / 2
x2 = dis_width / 2
y2 = dis_height / 2
x1_change = 0
y1_change = 0
x2_change = 0
y2_change = 0
snake_List = []
Length_of_snake = 1
#creo el cuadrado
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()

#tamaño de la serpiente
player1 = 10
player2 = 10

#velocidad de la serpiente
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
#funcion serpiente. tamaño del bloque y lista.

#def our_snake(snake_block, snake_list):

#dibujo los cuadrados de la serpiente. X son las coordenadas de cada bloque.:
pygame.draw.rect(dis, black, [x1[0], x1[1], player1, player1])
for x in range(player2):
    pygame.draw.rect(dis, red, [x[0], x[1], player2, player2] )
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
#funcion loop principal.
def gameLoop():
    game_over = False
    game_close = False
 
 #inicio de la serpiente.
    x1 = dis_width / 2
    y1 = dis_height / 2
    x2 = dis_width / 2
    y2 = dis_height / 2
    x1_change = 0
    y1_change = 0
    x2_change = 0
    y2_change = 0
    snake_List = []
    Length_of_snake = 1
 
 #comida.
    #foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    #foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
 #loop mientras hay juego.
    while not game_over:
 
 #loop de juego acabado.
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
 
            pygame.display.update()
 #espero a que se teclee algo. si controlQ, se acaba. si ControlC, vuelvo a empezar.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 #eventos de las teclas de direccion. x1_change y y1_change es +/- 10 hacia donde se haya tecleado.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -player1
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = player1
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -player1
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = player1
                    x1_change = 0
                    #controles jugador 2
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -player2
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = player2
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -player2
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = player2
                    x1_change = 0







 #si se toca la pared, se acaba el juego.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        #x1 = x1 + x1_change
        y1 += y1_change
        #y1 = y1 + y1_change.
        
        #relleno de azul
        dis.fill(blue)
        #dibujo comida.
        #pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        #vector con coordenada de la cabeza de serpiente.
        #snake_Head = []
        
        #snake_Head.append(x1)
        #snake_Head.append(y1)
        #añado la cabeza a la lista de la serpiente.
        #snake_List.append(snake_Head)
        
        #si la longitud de la lista es mayor que la variable longitud, quito el primer elemento de la lista ?? Por tanto el último elemento es la cabeza.
       #if len(snake_List) > Length_of_snake:
        #    del snake_List[0]
 
        #repaso toda la lista menos la cabeza. esto es para cuando la serpiente choca consigo misma.
       # for x in snake_List[:-1]:
      #      if x == snake_Head:
       #         game_close = True
        #dibujo la serpiente
        #our_snake(snake_block, snake_List)
 
 
        pygame.display.update()
 
        #si me como una comida, creo una nueva comida y aumento la longitud de la serpiente en 1.
       # if x1 == foodx and y1 == foody:
        #    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
         #   foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
          #  Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()