import pygame , random
pygame.mixer.pre_init(frequency = 44100 , size =16 , channels = 1 , buffer = 512)
from pygame import mixer
mixer.init()
pygame.init()
score = 0
highscore= 0
gameFont = pygame.font.Font("best.ttf" , 15)
abtMeFont = pygame.font.Font("nice.ttf" , 20)
gameOverFont = pygame.font.Font("best.ttf" , 40)

def landDraw():
    screen.blit(landImg , (landX , 400+20))
    screen.blit(landImg , ( screen_width , 400))
def pipeCreate():
    randomPipePos = random.choice(pipeHeight)
    pipeRectUp = pipeImg.get_rect( midtop = (400 , randomPipePos))
    pipeRectDown = pipeImg.get_rect(midbottom = (400 , randomPipePos - 150))
    return pipeRectUp , pipeRectDown
    
    return pipeRect
def pipeMotion(pipes):
    for pipe in pipes:
        pipe.centerx-=2
    return pipes
def pipeBlit(pipes):
    for pipe in pipes:
        if pipe.bottom >= screen_height:
             screen.blit(pipeImg , pipe)
        else:
            reversedPipe = pygame.transform.flip(pipeImg ,False , True)
            screen.blit(reversedPipe , pipe)
def rotatingBird(flappy):
    rotBird = pygame.transform.rotozoom(flappy , -birdMove * 3 , 1)
            
    return rotBird
def checkCollision(pipes):
    for pipe in pipes:
        if birdRect.colliderect(pipe):
            hitSound()
            
            return False
        
    
    if birdRect.top <= -50 or birdRect.bottom >= 400:
        hitSound()
       
        return False
    return True
def scoreDisplay(status):
    if status == "active":
        scoreFont = gameFont.render(f"score: {int(score)}" , True , (255 , 255 ,255))
        screen.blit(scoreFont , (100 , 10))
    if status == "inactive":
        scoreFont = gameFont.render(f"score: {int(score)}" , True , (255 , 255 ,255))
        
        
        screen.blit(scoreFont , (100 , 10))
        
        highscoreFont = gameFont.render(f"Highscore: {int(score)}" , True , (255 , 255 ,255))
      
        screen.blit(highscoreFont , (100 , 400))
        
def updateScore(score , highscore):
    if score > highscore:
        highscore = score 
    return highscore
def displayGameOver(x , y):
    gameOverTxt = gameOverFont.render("GAME OVER" , True , (255 , 255 , 60))
    screen.blit(gameOverTxt , (x , y))
def displayInfo(x , y):
    displayInfo = gameFont.render("-->TAP SPACE START" ,True , (255 , 0 , 0))
    screen.blit(displayInfo , (x , y))
def flySound():
    flySounds = pygame.mixer.Sound("fly.wav")
    flySounds.play()
def hitSound():
    hitSounds = pygame.mixer.Sound("hit.wav")
    hitSounds.play()
def abtTheDev(x , y):
    abtTxt = abtMeFont.render("DEV BY--> KINFE" , True , (0 , 0 , 0))
    screen.blit(abtTxt , (x , y))
screen_height = 512
screen_width = 288

gravity = 0.25
birdMove = 0


bgMusic = mixer.music
bgMusicUpdate = bgMusic.load("bgmusic.wav")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width , screen_height))
iconImg = pygame.image.load("flappy.png")
pygame.display.set_icon(iconImg)
bgImg = pygame.image.load("bgday.png")
landImg = pygame.image.load("land.png")
landImgSec = pygame.image.load("land.png")
flappyBird = pygame.image.load("actualBird.png")
pipeImg = pygame.image.load("pipeGreenLarge.png")

pipeList = []
pipeHeight = [200 , 300 , 400]
PIPECREATION = pygame.USEREVENT
pygame.time.set_timer(PIPECREATION , 1200)
birdRect = flappyBird.get_rect(center = (50 , 256))
landX = 0;


onGame = True

pygame.display.set_caption("KINFISH FLAPPY BIRD GAME ")
pygame.mixer.music.load("bgmusic.wav")
pygame.mixer.music.play(-1)
run = True
while run:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and onGame:
                flySound()
                birdMove = 0
                birdMove = -6
            if event.key == pygame.K_SPACE and onGame == False:
                
                score = 0
                onGame = True
                pipeList.clear()
                birdRect.center = (50 , 256)
                birdMove = 0
        if event.type == PIPECREATION:
            pipeList.extend(pipeCreate())
            
      
 
    #IMAGE CREATION 
    screen.blit(bgImg , (0, 0))
    if onGame:
        
        birdMove += gravity
        rotatedBird = rotatingBird(flappyBird)
        birdRect.centery += birdMove
        screen.blit(rotatedBird , birdRect)
        onGame = checkCollision(pipeList)
        
        #PIPE MANIPULATING 
        pipeList = pipeMotion(pipeList)
        pipeBlit(pipeList)
        
        score += 0.01
        
        scoreDisplay("active")
        
    else:
        displayGameOver(30 , 256)
        displayInfo(100 , 300)
        abtTheDev(80 , 346 )
        highscore = updateScore(score , highscore)
        scoreDisplay("inactive")
 
    
    #LAND MOTIONS
    landX-=1    
    landDraw()
    if landX < -(screen_width/6):
        landX = 0
       
   
        
    
    
    
    
    
    
    
    pygame.display.update()
    clock.tick(120)
            
pygame.quit()