import pygame
from pygame.sprite import Sprite
import random
class nCoV(Sprite):
    def __init__(self, settings, screen,img_path,index,stats,life,speed):
        super(nCoV,self).__init__()
        self.screen = screen
        self.settings = settings
        # 记载礼物属性
        self.index = index

        #加载病毒图像，并设置其rect属性
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #随机生成位置
        self.rect.x = random.randint(0,self.screen_rect.width-self.rect.width)
        self.rect.y = random.randint(-1000*(stats.level/5),100)

        #储存外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动次数
        self.count = 0
        # 方向
        self.direction = 0
        # 生命
        self.life = life
        # 绘制生命
        self.prep_life()

        self.speed = self.settings.ncov_speed_list[speed]

    def prep_life(self):
        font = pygame.font.SysFont(None, 40)
        self.life_image = font.render(str(self.life), True, (255, 0, 0), None)
        self.life_image_rect = self.life_image.get_rect()

        self.life_image_rect.centerx = self.rect.left
        self.life_image_rect.centery = self.rect.top


    def blitme(self):
        """在指定的位置绘制病毒"""
        self.screen.blit(self.life_image, self.life_image_rect)
        self.screen.blit(self.image,self.rect)



    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= self.screen_rect.height - self.rect.height:
            self.rect.top = self.screen_rect.height - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <=0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
    def moveRight(self):
        if self.rect.left  >= self.screen_rect.width - self.rect.width:
            self.rect.left  = self.screen_rect.width - self.rect.width
        else:
            self.rect.left  += self.speed

    def update(self):
        """向左或向右移动病毒"""
        # self.rect.centery += self.settings.ncov_speed
        if self.count >5:
            self.count = 0
            self.direction = random.randint(1,9)
        else:
            if self.direction == 1:
                self.moveUp()
            elif self.direction ==2:
                self.moveDown()
            elif self.direction ==3:
                self.moveLeft()
            elif self.direction ==4:
                self.moveRight()
            elif self.direction ==5:
                self.moveUp()
                self.moveLeft()
            elif self.direction ==6:
                self.moveUp()
                self.moveRight()
            elif self.direction ==7:
                self.moveDown()
                self.moveRight()
            elif self.direction ==8:
                self.moveDown()
                self.moveLeft()

            self.moveDown()
            self.count +=1


        # kx = random.randint(0,1)
        # ky = random.randint(0,1)
        # if kx and self.rect.x < self.screen_rect.width-self.rect.width:
        #     self.rect.centerx += 2
        # if kx!=1 and self.rect.x >0:
        #     self.rect.centerx -= 2
        # if ky and self.rect.y < self.screen_rect.height-self.rect.height:
        #     self.rect.centery += 2
        # if ky!=1 and self.rect.y > 0:
        #     self.rect.centery -= 2
        # self.y+= 1
        # self.rect.y = self.y


