#Comments
import pygame
import random
import os
# from Reading_Functions import readBall,readPaddle
# initialize pygame

pygame.init()
pygame.mixer.init()
# set the height and width of the screen

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Sprites')
# import paddles here
paddleSprite = pygame.image.load(os.path.join(img_folder, 'Spritealpha.png')).convert()
paddleSpriteCranberry = pygame.image.load(os.path.join(img_folder, 'spritecranalpha.png')).convert()
paddleCranberryDry = pygame.image.load(os.path.join(img_folder, 'Canada Dry Cranberry-1.png.png')).convert()
paddleDry = pygame.image.load(os.path.join(img_folder, 'Canada Dry-1.png.png')).convert()
paddleCoca = pygame.image.load(os.path.join(img_folder, 'cocacola.png')).convert()
paddleFanta = pygame.image.load(os.path.join(img_folder, 'fanta.png')).convert()
paddleMDEWC = pygame.image.load(os.path.join(img_folder, 'mountain dew cranberry-1.png.png')).convert()
paddleMDEW = pygame.image.load(os.path.join(img_folder, 'mountain dew-1.png.png')).convert()
paddlePep1 = pygame.image.load(os.path.join(img_folder, 'pepsi.png')).convert()

# import balls here
ball1 = pygame.image.load(os.path.join(img_folder, 'redball18x18.png'))
ball2 = pygame.image.load(os.path.join(img_folder, 'ball sprite-1.png.png'))
ball3 = pygame.image.load(os.path.join(img_folder, 'Trump for ball-1.png.png'))

#music
pygame.mixer.music.load('Trance - 009 Sound System Dreamscape.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

# Insert all the ball choices here

WHITE = (255, 255, 255)

BACKGROUND = (0, 100, 255)

font = pygame.font.SysFont(None, 24)

def textScreen(writtentext):
    text = font.render(writtentext, True, WHITE, BACKGROUND)
    textRect = text.get_rect()
    textRect.centerx = screen_width/2
    textRect.centery = screen_height/2
    screen.blit(text, textRect)

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.fill(BACKGROUND)
                    run = False


def showText(text):
    t = font.render(text, True, WHITE, BACKGROUND)
    tRect = t.get_rect()
    tRect.centerx = 250
    tRect.centery = 250
    screen.blit(t, tRect)

    pygame.display.flip()

#################### Main program starts here
run = True

screen.fill(BACKGROUND)

textScreen("Welcome to Pong Game! Press Enter to continue...")
textScreen("Player 1: Use the up and down arrows to move the paddle")
textScreen("Player 2: Use the W and S keys to move the paddle")
textScreen("Goal: don't let ball beyond the paddle, first to 5 points wins")
textScreen("Good luck!")
textScreen("Go to the console to enter your paddle choices. press enter.")


UP = 1
DOWN = -1
FLAT = 0

RIGHT = 1
LEFT = -1

score1 = 0
score2 = 0
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.direction = FLAT  # 0: no move, 1: moving up: -1: moving down

    # Reading chosen sprites
    def readPaddle(self):

        paddleChoice = input("Choose a paddle 1/2/3/4/5/6/7/8/9: ")
        try:
            if paddleChoice is "1":
                self.image = paddleSprite
            if paddleChoice is "2":
                self.image = paddleSpriteCranberry
            if paddleChoice is "3":
                self.image = paddleCranberryDry
            if paddleChoice is "4":
                self.image = paddleDry
            if paddleChoice is "5":
                self.image = paddleCoca
            if paddleChoice is "6":
                self.image = paddleFanta
            if paddleChoice is "7":
                self.image = paddleMDEWC
            if paddleChoice is "8":
                self.image = paddleMDEW
            if paddleChoice is "9":
                self.image = paddlePep1


            self.rect = self.image.get_rect()
            self.image.set_colorkey((255, 255, 255))
            self.image.set_colorkey((0, 0, 0))
        except ValueError or AttributeError:
            print("Value not accepted")

    def moveUp(self, pixels):
        self.rect.y -= (pixels * 1.1)
        self.direction = UP

    def moveDown(self, pixels):
        self.rect.y += (pixels * 1.1)
        self.direction = DOWN

    def stop(self):
        self.direction = FLAT


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.xstep = 5  # positive: moving to the right, negative: moving to the left
        self.ystep = 0  # 0: no move, positive: moving down: negative: moving up

    def ballpos(self):
        self.rect.x = screen_width/2
        self.rect.y = screen_height/2

    def readball(self):
        ballChoice = input("Choose a ball 1/2/3: ")
        try:
            if ballChoice is "1":
                self.image = ball1
            if ballChoice is "2":
                self.image = ball2
            if ballChoice is "3":
                self.image = ball3

            self.rect = self.image.get_rect()
            self.image.set_colorkey((255, 255, 255))
        except ValueError or AttributeError:
            print("Value not accepted")

    def ballreset(self):
        self.rect.x = screen_width/2
        self.rect.y = screen_height/2
        self.xstep = 5
        self.ystep = 0


    def moveball(self, yDirection):
        self.rect.x += self.xstep

        if (yDirection == UP): # move up screen
            self.ystep = -5
        elif (yDirection == DOWN): # move down screen
            self.ystep = 5

        if (self.rect.y <= 0) or (self.rect.y >= screen_height): # if it reaches the bottom or the top of the screen
            self.reverseY()

        self.rect.y += self.ystep

    def reverseX(self):
        self.xstep *= -1.1

    def reverseY(self):
        self.ystep *= -1.1

all_sprites_list = pygame.sprite.Group()

player1 = Player()
player2 = Player()
player1.readPaddle()
player2.readPaddle()
player1.rect.x = 10
player1.rect.y = screen_height/2
player2.rect.x = screen_width-50
player2.rect.y = screen_height/2


ball12 = Ball()
ball12.readball()
ball12.ballpos()
ball12.moveball(FLAT)

all_sprites_list.add(player1, player2, ball12)

clock = pygame.time.Clock()
turn_done = False

while run:
    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.constants.USEREVENT:
            pygame.mixer.music.load('Trance - 009 Sound System Dreamscape.mp3')
            pygame.mixer.music.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2.moveUp(5)
        if player2.rect.y <= 0:
            player2.rect.y = 0
    if keys[pygame.K_DOWN]:
        player2.moveDown(5)
        if player2.rect.y >= screen_height - player2.rect.height:
            player2.rect.y = screen_height - player2.rect.height
    if keys[pygame.K_w]:
        player1.moveUp(5)
        if player1.rect.y <= 0:
            player1.rect.y = 0
    if keys[pygame.K_s]:
        player1.moveDown(5)
        if player1.rect.y >= screen_height - player1.rect.height:
            player1.rect.y = screen_height - player1.rect.height

    ball12.moveball(FLAT)
    if pygame.sprite.collide_rect(ball12, player2):
        ball12.reverseX()
        ball12.moveball(player2.direction)

    elif pygame.sprite.collide_rect(player1, ball12):
        ball12.reverseX()
        ball12.moveball(player1.direction)

    # P1 scores a point
    if ball12.rect.x >= screen_width - 10:
        ball12.ballreset()
        score1 += 1
        turn_done = True
        if turn_done:
            textScreen("Player 1 has scored! Press ENTER to continue")
            turn_done = False

    elif ball12.rect.x <= 10:
        ball12.ballreset()
        score2 += 1
        turn_done = True
        if turn_done:
            textScreen("Player 2 has scored! Press ENTER to continue")
            turn_done = False

    # Print the score  :)
    scoreprint = "Player 1: " + str(score1)
    text = font.render(scoreprint, 1, WHITE)
    textpos = (0, 0)
    screen.blit(text, textpos)

    scoreprint = "Player 2: " + str(score2)
    text = font.render(scoreprint, 1, WHITE)
    textpos = (screen_width - 100, 0)
    screen.blit(text, textpos)

    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.update()
    clock.tick(60)
    if score1 == 5:
        run = False
        screen.fill(BACKGROUND)
        textScreen("Game over, Player 1 wins")
    if score2 == 5:
        run = False
        screen.fill(BACKGROUND)
        textScreen("Game over, Player 2 wins")
pygame.quit()
