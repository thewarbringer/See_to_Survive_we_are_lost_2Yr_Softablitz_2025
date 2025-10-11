import pygame 
import random
from pygame import mixer
pygame.init()
mixer.init()


gameWindow = pygame.display.set_mode((1200,600))
pygame.display.set_caption("See To Survive")
pygame.display.update()
######################################################################################
######################################################################################
######################################################################################
isinplay = False
#game specific variables
pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 64)
coin_sound= mixer.Sound("resources/music/coin.mp3")
aah_sound = mixer.Sound("resources/music/aah.mp3")
one_up_sound = mixer.Sound("resources/music/oneup.mp3")
mixer.music.load("resources/music/thunder.mp3")
mixer.music.set_volume(1)
mixer.music.play(-1)
char_image = [pygame.image.load('resources/images/s1.png'),pygame.image.load("resources/images/s2.png"),pygame.image.load("resources/images/s3.png"),pygame.image.load("resources/images/s4.png"),pygame.image.load("resources/images/s5.png"),pygame.image.load("resources/images/s6.png")]
colors = [(0,0,0),(255,0,0),(255,255,0),(0,255,0),(0,150,0)]    #colors for healthbar
exit_game = False
game_over = False
ch_x1 = 300 #POSITION OF CHARACTER IN X
ch_y1 = 500  #POSITION OF CHARACTER IN Y
ch_x2 = 300 #POSITION OF CHARACTER IN X
ch_y2 = 500  #POSITION OF CHARACTER IN Y

ch_size = 50 #SIZE OF SPRITE
score1 = 0       #user's score1 is counted here
score2 = 0       #user's score1 is counted here

clock = pygame.time.Clock() #clock for ticking
cc = 0;             
shield =0
waves_for_shield1 = 4
isShield1 = False
shield_waiter1 = 0
waves_for_shield2 = 4
isShield2 = False
shield_waiter2 = 0

waiter = 5              #waiter is for speed, less waiter => high speed
original_waiter = 5     #waiter resets to original waiter    
m1=0             #state of flame
ud1 = 0          #to prevent instant state change to 4
hogaya1 = 0      #to prevent instant level change to max
amber_count1 = 0
amber_waiter1 = 0
m2=0             #state of flame
ud2 = 0          #to prevent instant state change to 4
hogaya2 = 0      #to prevent instant level change to max
amber_count2 = 0
amber_waiter2 = 0

empty = 7 #initial setting of the zeroes in matrix
counter_of_waves=1
matrix = [0,0,0,0,0,0,0,0,0,0,0,0] #matrix for the drops
amb = 0
backs = [pygame.image.load("resources/images/back1.png"),pygame.image.load("resources/images/back2.png"),pygame.image.load("resources/images/back3.png"),pygame.image.load("resources/images/back4.png"),pygame.image.load("resources/images/back5.png"),pygame.image.load("resources/images/back6.png")]
amber = pygame.image.load("resources/images/amber.png")
drops = [pygame.image.load("resources/images/dropsmall.png"),pygame.image.load("resources/images/dropbig.png")]
shield_img = pygame.image.load("resources/images/shield.png")
        
def draw_drops():
    for i in range(12):
        if matrix[i] != 0 :
            gameWindow.blit(drops[matrix[i]-1],(50*i,cc*50))
    for i in range(12):
        if matrix[i] != 0 :
            gameWindow.blit(drops[matrix[i]-1],(50*i+600,cc*50))
    
def generate_amber():
    global amb
    global amber_waiter2
    global amber_waiter1 
    if(amber_waiter1 == 0):
        if (score1%6==0) :
            amber_waiter1 = 48;
            amber_waiter2 = 48;
            
            k = random.randint(0,11)
            amb = k 

def generate_shield():
    global shield
    global shield_waiter1 
    global shield_waiter2 
    if(shield_waiter2 == 0):
        if score1!=0 and score1!=1 and (score1%7==0) :
            shield_waiter2 = 48;
            shield_waiter1 = 48;
            k = random.randint(0,11)
            shield = k 
def fill_matrix():
    global empty
    global score1
    global original_waiter
    if score1%11 == 0:
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

currentCharacterLocation2 = 6;
currentCharacterLocation1 = 6;
currentCharacterState = 1;
pp1=0
pp2=0
uph1 = 0
high_score1 = 1












######################################################################################
######################################################################################
######################################################################################
def gameStart():    
    global exit_game
    global uph1
    global cc,ud1,pp1,currentCharacterLocation1,currentCharacterState
    global m1,hogaya1,high_score1
    global waiter,original_waiter
    global game_over
    global score1
    global isShield1,matrix
    global ch_x1,ch_y1
    global amber_count1,amber,amb,amber_waiter1
    global shield,shield_waiter1,isShield1,waves_for_shield1
    global exit_game
    
    global uph1
    global cc,ud2,pp2,currentCharacterLocation2
    global m2,hogaya2
    global waiter,original_waiter
    global game_over
    global score2
    global isShield2,matrix
    global ch_x2,ch_y2
    global amber_count2,amber,amb,amber_waiter2
    global shield,shield_waiter2,isShield2,waves_for_shield2
    while not exit_game :
        if(uph1 != 1):
            uph1 =1;
        if(cc == 1):
            gameWindow.blit(backs[4],(0,0))
            gameWindow.blit(backs[4],(600,0))
        elif cc == 2:
            gameWindow.blit(backs[5],(0,0))
            gameWindow.blit(backs[5],(600,0))
        else:
            gameWindow.blit(backs[m1],(0,0))
            gameWindow.blit(backs[m2],(600,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    original_waiter=5
                    shield=0
                    shield_waiter1=0
                    isShield1=0
                    waves_for_shield1=0
                    amber_count1=0
                    amber_waiter1=0
                    ch_x1=300
                    waiter=5
                    game_over=False
                    uph1=0
                    cc=0
                    ud1=0
                    pp1=0
                    m1=0
                    currentCharacterLocation1=6
                    matrix = [0,0,0,0,0,0,0,0,0,0,0,0]
                    score1=0
                    
                    shield_waiter2=0
                    isShield2=0
                    waves_for_shield2=0
                    amber_count2=0
                    amber_waiter2=0
                    ch_x2=300
                    waiter=5
                    game_over=False
                    uph1=0
                    cc=0
                    ud2=0
                    pp2=0
                    m2=0
                    currentCharacterLocation2=6
                    matrix = [0,0,0,0,0,0,0,0,0,0,0,0]
                    
            if event.type == pygame.KEYDOWN and (not game_over):
                
                if event.key == pygame.K_RIGHT and ch_x2 < 550  :
                    ch_x2 = ch_x2 + 50;
                    currentCharacterLocation2 = currentCharacterLocation2+1
                if event.key == pygame.K_LEFT and ch_x2 > 0 and (not game_over):
                    ch_x2 = ch_x2 - 50
                    currentCharacterLocation2 = currentCharacterLocation2-1
                if event.key == pygame.K_d and ch_x1 < 550  :
                    ch_x1 = ch_x1 + 50;
                    currentCharacterLocation1 = currentCharacterLocation1+1
                if event.key == pygame.K_a and ch_x1 > 0 and (not game_over):
                    ch_x1 = ch_x1 - 50
                    currentCharacterLocation1 = currentCharacterLocation1-1
    
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
        
        if isShield1:
            gameWindow.blit(char_image[5],(ch_x1,ch_y1))
        else:
            gameWindow.blit(char_image[m1],(ch_x1,ch_y1))
        if isShield2:
            gameWindow.blit(char_image[5],(ch_x2+600,ch_y1))
        else:
            gameWindow.blit(char_image[m2],(ch_x2+600,ch_y1))
        
        pygame.draw.rect(gameWindow,(255,255,255),(50,45,160,30))
        pygame.draw.rect(gameWindow,(255,0,255),(55,50,(50*amber_count1),20))
        pygame.draw.rect(gameWindow,(255,255,255),(375,45,210,30))
        pygame.draw.rect(gameWindow,colors[4-m1],(380,50,50*(4-m1),20))
        pygame.draw.rect(gameWindow,(255,255,255),(50+600,45,160,30))
        pygame.draw.rect(gameWindow,(255,0,255),(55+600,50,(50*amber_count2),20))
        pygame.draw.rect(gameWindow,(255,255,255),(375+600,45,210,30))
        pygame.draw.rect(gameWindow,colors[4-m2],(380+600,50,50*(4-m2),20))
        
        if(amber_waiter1 > 0):
            gameWindow.blit(amber,(amb*50,550))
            amber_waiter1 = amber_waiter1 - 1
        if(shield_waiter1 > 0):
            gameWindow.blit(shield_img,(shield*50,550))
            shield_waiter1 = shield_waiter1 - 1
        if(amber_waiter2 > 0):
            gameWindow.blit(amber,(600+amb*50,550))
            amber_waiter2 = amber_waiter2 - 1
        if(shield_waiter2 > 0):
            gameWindow.blit(shield_img,(600+shield*50,550))
            shield_waiter2 = shield_waiter2 - 1


        if game_over:
            rest = pygame.image.load("resources/images/resta2.png")
            gameWindow.blit(rest,(0,0))
            if m2 == m1:
                texti = "Draw"
                text_surface = my_font.render(texti, False, (55, 55, 255))
                gameWindow.blit(text_surface, (450,250))
            elif m2 == 5:
                texti = "Player 2 lost"
                text_surface = my_font.render(texti, False, (55, 55, 255))
                gameWindow.blit(text_surface, (350,250))
            else :
                texti = "Player 1 lost"
                text_surface = my_font.render(texti, False, (55, 55, 255))
                gameWindow.blit(text_surface, (350,250))
            
        pygame.display.update()

        clock.tick(24)
##################################################################
        if(score1 == 0):
            k=0
        else:
            k=1
        if(cc == 2):
            generate_amber()
        if(cc == 0):
            generate_shield()
##############################################################33
        if(cc == 12 and pp1 ==0):
            pp1=1
            waves_for_shield1 = waves_for_shield1 -1 
        if(cc == 12 and pp2 ==0):
            pp2=1
            waves_for_shield2 = waves_for_shield2 -1 
###################################################################3
        if waves_for_shield1 <= 0:
            isShield1 = False  
        if(cc == 12):
            pp1 =0
            ud1 = 0
            cc = 0
            pp2 =0
            ud2 = 0
            score1 = score1 + 1
        
        if waves_for_shield2 <= 0:
            isShield2 = False  
        
            
#############################################################33
        if(currentCharacterLocation1 == amb and amber_waiter1>0):
            amber_waiter1 = 0
            amber_count1 = amber_count1+1
            if(amber_count1 == 3):
                one_up_sound.play()
                amber_count1= 0
                if(m1!= 0):
                    m1 = m1 -1
            else:
                coin_sound.play()
        if(currentCharacterLocation2 == amb and amber_waiter2>0):
            amber_waiter2 = 0
            amber_count2 = amber_count2+1
            if(amber_count2 == 3):
                one_up_sound.play()
                amber_count2= 0
                if(m2!= 0):
                    m2 = m2 -1
            else:
                coin_sound.play()
#########################################################################################
        if(currentCharacterLocation1 == shield and shield_waiter1>0 and not isShield1):
            waves_for_shield1 = 4
            isShield1 = True
            shield_waiter1 = 0
            coin_sound.play()
        if(currentCharacterLocation2 == shield and shield_waiter2>0 and not isShield2):
            waves_for_shield2 = 4
            isShield2 = True
            shield_waiter2 = 0
            coin_sound.play()
#########################################################################################33333
        if(cc == 11 and ud1 == 0):
            if(matrix[currentCharacterLocation1]!=0 and ud1 ==0 and not game_over and not isShield1):
                aah_sound.play()
            if((m1+matrix[currentCharacterLocation1]) <= 5 and not isShield1):
                if((m1+matrix[currentCharacterLocation1])==5):
                    m1 = 4
                    ud1 = 1
                else:
                    m1 = m1 + matrix[currentCharacterLocation1]
                    
                    print("--------------------")
                    ud1=1
        if(m1 == 4):
            game_over=True
        
        
        if(cc == 11 and ud2 == 0):
            if(matrix[currentCharacterLocation2]!=0 and ud2 ==0 and not game_over and not isShield2):
                aah_sound.play()
            if((m2+matrix[currentCharacterLocation2]) <= 5 and not isShield2):
                if((m2+matrix[currentCharacterLocation2])==5):
                    m2 = 4
                    ud2 = 1
                else:
                    m2 = m2 + matrix[currentCharacterLocation2]
                    
                    print("--------------------")
                    ud2=1

        if(m2 == 4):
            game_over=True




        if(score1%3 == 0) and hogaya1 ==0 and original_waiter > 1:
            original_waiter = original_waiter - 1;
            hogaya1 = 1
        if(score1%3 != 0):
            hogaya1 = 0;
        print(ud1)
        print(ud2)
        print(matrix)
        print(isShield2)
        print(currentCharacterLocation2)
######################################################################################
######################################################################################
######################################################################################

gameStart()

pygame.quit()
