import pygame
from pygame.sprite import Sprite
class Wbc(Sprite):
    def __init__(self,settings, screen):
        super(Wbc, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load(settings.wbc_image_path[0])

        self.rect = self.image.get_rect()  # 获取图片外接矩形
        self.screen_rect = screen.get_rect()

        # 将病毒放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """绘制白细胞"""
        self.screen.blit(self.image, self.rect)

    def blitme_play(self,image_path):
        """绘制白细胞"""
        image = pygame.image.load(image_path)
        self.screen.blit(image, self.rect)
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.settings.wbc_speed

    def moveDown(self):
        if self.rect.top >= self.screen_rect.height - self.rect.height:
            self.rect.top = self.screen_rect.height - self.rect.height
        else:
            self.rect.top += self.settings.wbc_speed

    def moveLeft(self):
        if self.rect.left <=0:
            self.rect.left = 0
        else:
            self.rect.left -= self.settings.wbc_speed
    def moveRight(self):
        if self.rect.left  >= self.screen_rect.width - self.rect.width:
            self.rect.left  = self.screen_rect.width - self.rect.width
        else:
            self.rect.left  += self.settings.wbc_speed
    def update(self):
        """根据移动标志调整位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.wbc_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.wbc_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.wbc_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.wbc_speed
