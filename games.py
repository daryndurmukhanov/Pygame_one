import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
surface = pygame.Surface((500, 500))
clock = pygame.time.Clock()

PlayerStand = pygame.image.load('idle.png')

walkRight = [pygame.image.load('right_1.png'), pygame.image.load('right_2.png'), pygame.image.load('right_3.png'), pygame.image.load('right_4.png'), pygame.image.load('right_5.png'), pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'), pygame.image.load('left_3.png'), pygame.image.load('left_4.png'), pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]
done = False

x = 50
y = 425
width = 60
height = 71
speed = 5 

bg = pygame.image.load('bg.jpg')

jumpCound = 10
is_jump = False

left = False
right = False
animCount = 0
lastMove = "right"

class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def drawWindow():
    global animCount
    screen.blit(bg, (0, 0)) 
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        screen.blit(walkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right:
        screen.blit(walkRight[animCount // 5], (x,y))
        animCount += 1
    else:
        screen.blit(PlayerStand, (x, y))

    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()
    
bullets = []   
while not done:
        clock.tick(30)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        for bullet in bullets:
            if bullet.x < 500 and bullet.x >0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_f]:
            if lastMove == "right":
                facing = 1
            else:
                facing = -1
            if len(bullets) < 5:
               bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing ))

        if pressed[pygame.K_LEFT] and x > 5: 
            x -= speed
            left = True
            right = False
            lastMove = "left"
        
        elif pressed[pygame.K_RIGHT] and x < 500 - width - 5: 
            x += speed
            left = False
            right = True
            lastMove = "right"
        else:
            left = False
            right = False
            animCount = 0
        if not(is_jump):
            if pressed[pygame.K_SPACE]:
                  is_jump = True
        else:
                if jumpCound >= -10:
                        if jumpCound < 0:
                                y += (jumpCound**2)/2
                        else:
                                y -= (jumpCound**2) / 2
                        jumpCound -=1

                else:
                   is_jump = False
                   jumpCound = 10       
        drawWindow()
        