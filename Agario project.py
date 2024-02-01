'''
Tutorial demonstrates how to create a game window with Python Pygame.

Any pygame program that you create will have this basic code
'''

import pygame, sys, random, math

class Food(pygame.sprite.Sprite):
    #Constructor
    def __init__(self,color):
        super(Food,self).__init__() #calling on the constructor for the Sprite class
        
        self.radius = 8
        self.image=pygame.Surface((self.radius*2,self.radius*2),pygame.SRCALPHA,32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image,color,(self.radius,self.radius),self.radius)
        self.rect=self.image.get_rect(center=(random.randint(3,1397),random.randint(3,797)))

    def relocate(self):
        self.rect.center=(random.randint(3,797),random.randint(3,597))

class Player(pygame.sprite.Sprite):
    def __init__(self,color):
        super(Player,self).__init__()

        self.radius = 25
        self.image=pygame.Surface((self.radius*2,self.radius*2),pygame.SRCALPHA,32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image,color,(self.radius,self.radius),self.radius)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.color= (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        self.radius = random.randint(20,50)
        self.image=pygame.Surface((self.radius*2,self.radius*2),pygame.SRCALPHA,32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image,self.color,(self.radius,self.radius),self.radius)
        self.rect=self.image.get_rect(center=(random.randint(50,750),random.randint(50,550)))
        
        self.delta_x=random.choice([-1,1])
        self.delta_y=random.choice([-1,1])
        self.speed=100/self.radius
    def move(self):
        self.rect.centerx+=self.delta_x*self.speed
        self.rect.centery+=self.delta_y*self.speed
        
        if self.rect.centerx+self.radius>=800 or self.rect.centerx-self.radius<=0:
            
        
            self.delta_x*=-1
        if self.rect.centery+self.radius>=600 or self.rect.centery-self.radius<=0:
            
            self.delta_y*=-1
    def grow(self, growsize):
        self.radius+=growsize
        self.image=pygame.Surface((self.radius*2,self.radius*2),pygame.SRCALPHA,32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image,self.color,(self.radius,self.radius),self.radius)
        self.speed=100/self.radius
    def collision_detector(self,other):
        xdist=self.rect.centerx-other.rect.centerx
        ydist=self.rect.centery-other.rect.centery
        if math.sqrt((xdist**2)+(ydist**2))<=other.radius+self.radius:
            return True
        else:
            return False
        
        

    
        
# Initialize Pygame and give access to all the methods in the package
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")


WHITE= (255,255,255)
BLUE=(0,0,255)
clock = pygame.time.Clock()

meals=pygame.sprite.Group() #group is high powered list
for num in range (20):
    meals.add(Food("red"))

enemies=pygame.sprite.Group()
for num in range (5):
    enemies.add(Enemy())


running = True
while running:
    
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill("white")

    # for obj in objects
    #     for other in objects
    #         if obj!=other and type(obj)!=Food
    for i in enemies:
        

        i.move()

    #paste all food obj on screen
    #print(len(enemies))
    meals.draw(screen)
    enemies.draw(screen)

    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()