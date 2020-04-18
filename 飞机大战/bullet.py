import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹进行管理的类"""
    def __init__(self,settings,screen,wbc,img,life):
        """在白细胞所在的位置创建一个子弹对象"""
        super(Bullet,self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load(self.settings.bullet_image_path[img])

        # 获取图片外接矩形
        self.rect = self.image.get_rect()

        # 在白细胞的顶部中央生成子弹
        self.rect.centerx = wbc.rect.centerx
        self.rect.top = wbc.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.speed_factor = settings.bullet_speed_list[img]

        # 子弹生命
        self.life = life
    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y =self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        self.screen.blit(self.image, self.rect)