import pygame 
import random
from pygame import mixer
pygame.init()
mixer.init()

pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 30)
coin_sound= mixer.Sound("resources/music/coin.mp3")
aah_sound = mixer.Sound("resources/music/aah.mp3")
one_up_sound = mixer.Sound("resources/music/oneup.mp3")
mixer.music.load("resources/music/thunder.mp3")
mixer.music.set_volume(1)
mixer.music.play(-1)
gameWindow = pygame.display.set_mode((600,600))
pygame.display.set_caption("See To Survive")
pygame.display.update()

isinplay = False
#game specific variables
char_image = [pygame.image.load('resources/images/s1.png'),pygame.image.load("resources/images/s2.png"),pygame.image.load("resources/images/s3.png"),pygame.image.load("resources/images/s4.png"),pygame.image.load("resources/images/s5.png")]
colors = [(0,0,0),(255,0,0),(255,255,0),(0,255,0),(0,150,0)]    #colors for healthbar
exit_game = False
game_over = False
ch_x = 300 #POSITION OF CHARACTER IN X
ch_y = 500  #POSITION OF CHARACTER IN Y
ch_size = 50 #SIZE OF SPRITE
score = 0       #user's score is counted here
clock = pygame.time.Clock() #clock for ticking
cc = 0;               


waiter = 5              #waiter is for speed, less waiter => high speed
original_waiter = 5     #waiter resets to original waiter
wc = 1;
m=0             #state of flame
ud = 0          #to prevent instant state change to 4
hogaya = 0      #to prevent instant level change to max
amber_count = 0
amber_waiter = 0
empty = 7 #initial setting of the zeroes in matrix
counter_of_waves=1
matrix = [0,0,0,0,0,0,0,0,0,0,0,0] #matrix for the drops
amb = 0
backs = [pygame.image.load("resources/images/back1.png"),pygame.image.load("resources/images/back2.png"),pygame.image.load("resources/images/back3.png"),pygame.image.load("resources/images/back4.png"),pygame.image.load("resources/images/back5.png"),pygame.image.load("resources/images/back6.png")]
amber = pygame.image.load("resources/images/amber.png")
drops = [pygame.image.load("resources/images/dropsmall.png"),pygame.image.load("resources/images/dropbig.png")]

def update_high(score):
    a = open("resources/high.txt","r")
    k = a.read()
    s = int(k)
    if(score>s):
        a = open("resources/high.txt","w")
        a.write(str(score))
        
def draw_drops():
    for i in range(12):
        if matrix[i] != 0 :
            gameWindow.blit(drops[matrix[i]-1],(50*i,cc*50))

def generate_amber():
    global amb
    global amber_waiter 
    if(amber_waiter == 0):
        if m>0 and (score%6==0) :
            amber_waiter = 48;
            k = random.randint(0,11)
            amb = k 

def fill_matrix():
    global empty
    global score
    global original_waiter
    if score%11 == 0:
        if empty>=3:
            original_waiter = 3
            empty = empty-1
    for i in range(12):
        matrix[i] = random.randint(1,2)
    om=[0,1,2,3,4,5,6,7,8,9,10,11]
    for i in range(empty):
        k = random.choice(om)
        om.remove(k)
        matrix[k] = 0

currentCharacterLocation = 6;
currentCharacterState = 1;


uph = 0
a1 = open("resources/high.txt","r")
high_score = a1.read()
    
while not exit_game:
    if(uph != 1):
        uph =1;
    if(cc == 1):
        gameWindow.blit(backs[4],(0,0))
    elif cc == 2:
        gameWindow.blit(backs[5],(0,0))
    else:
        gameWindow.blit(backs[m],(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN and (not game_over):
            if event.key == pygame.K_RIGHT and ch_x < 550  :
                ch_x = ch_x + 50;
                currentCharacterLocation = currentCharacterLocation+1
            if event.key == pygame.K_LEFT and ch_x > 0 and (not game_over):
                ch_x = ch_x - 50
                currentCharacterLocation = currentCharacterLocation-1
    if(waiter == 0):
        if not game_over:
            waiter = original_waiter
            cc = cc +1
    else:
        if not game_over:
            waiter = waiter - 1    

    if(cc == 12):
        fill_matrix()
    if not game_over:
        draw_drops()
    texti = "Score :"+str(score)
    text_surface = my_font.render(texti, False, (155, 255, 255))
    text2 = "High Score :"+str(high_score)
    text_surface2 = my_font.render(text2, False, (155, 255, 255))
    
    gameWindow.blit(text_surface, (50,80))
    gameWindow.blit(text_surface2, (380,80))
    gameWindow.blit(char_image[m],(ch_x,ch_y))
    
    pygame.draw.rect(gameWindow,(255,255,255),(50,45,160,30))
    pygame.draw.rect(gameWindow,(255,0,255),(55,50,(50*amber_count),20))
    pygame.draw.rect(gameWindow,(255,255,255),(375,45,210,30))
    pygame.draw.rect(gameWindow,colors[4-m],(380,50,50*(4-m),20))
    if(amber_waiter > 0):
        gameWindow.blit(amber,(amb*50,550))
        amber_waiter = amber_waiter - 1
    pygame.display.update()
    if(cc == 12):
        ud = 0
        cc = 0
        score = score + 1
    clock.tick(24)
    if(score == 0):
        k=0
    else:
        k=1
    if(cc == 2):
        generate_amber()
    if(currentCharacterLocation == amb and amber_waiter>0):
        amber_waiter = 0
        amber_count = amber_count+1
        if(amber_count == 3):
            one_up_sound.play()
            amber_count= 0
            if(m!= 0):
                m = m -1
        else:
            coin_sound.play()
    if(cc == 11 and ud == 0):
        if(matrix[currentCharacterLocation]!=0 and ud ==0 and not game_over):
            aah_sound.play()
        if((m+matrix[currentCharacterLocation]) <= 5 ):
            if((m+matrix[currentCharacterLocation])==5):
                m = 4
                ud = 1
                
            else:
                m = m + matrix[currentCharacterLocation]
                ud=1

    if(m == 4):
        update_high(score)
        game_over=True
    
    if(score%3 == 0) and hogaya ==0 and original_waiter > 1:
        original_waiter = original_waiter - 1;
        hogaya = 1
    if(score%3 != 0):
        hogaya = 0;
pygame.quit()
