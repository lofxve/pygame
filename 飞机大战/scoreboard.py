import pygame.font
from pygame.sprite import Group

class Scoreboard():
    """显示得分信息的类"""
    def __init__(self, ai_settings, screen, stats):
         """初始化显示得分涉及的属性"""
         self.screen = screen
         self.screen_rect = screen.get_rect()
         self.ai_settings = ai_settings
         self.stats = stats


         # 显示得分信息时使用的字体设置
         self.text_color = (30, 30, 30)
         self.font = pygame.font.SysFont(None, 48)

         # 准备初始得分图像
         self.prep_score()
         self.prep_high_score()
         self.prep_level()
         self.prep_wbcs()
         self.prep_rank()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        score_str = str(self.stats.score)

        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render(score_str, True, self.text_color,self.ai_settings.bg_color)

         # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,self.text_color, self.ai_settings.bg_color)
        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""

        self.level_image = self.font.render(str(self.stats.level), True,self.text_color, self.ai_settings.bg_color)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()

        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_wbcs(self):
        """显示白细胞生命"""
        self.wbc_life = pygame.image.load(self.ai_settings.wbc_image_path[0])
        self.wbc_life_rect = self.wbc_life.get_rect()
        self.wbc_life_rect.left = self.screen_rect.left
        self.wbc_life_rect.top = self.screen_rect.top

        font = pygame.font.SysFont(None, 48)
        self.life_image = font.render(str(self.ai_settings.wbc_limit), True, (255,0,0), None)
        self.life_image_rect = self.life_image.get_rect()
        self.life_image_rect.centerx =  self.wbc_life_rect.centerx
        self.life_image_rect.centery = self.wbc_life_rect.centery

    def prep_rank(self):
        """显示段位"""
        if int(self.ai_settings.rank_in) >7:
            self.ai_settings.rank_in = 7
        self.rank_image = pygame.image.load(self.ai_settings.rank_in_images_path[int(self.ai_settings.rank_in)])
        self.rank_image_ract = self.rank_image.get_rect()

        self.rank_image_ract.right = self.screen_rect.right
        self.rank_image_ract.top = self.level_rect.top+ 50



    def show_score(self):
     """在屏幕上显示得分"""
     self.screen.blit(self.score_image, self.score_rect)
     self.screen.blit(self.high_score_image, self.high_score_rect)
     self.screen.blit(self.level_image, self.level_rect)
     self.wbc_life.blit(self.life_image, self.life_image_rect)
     self.screen.blit(self.wbc_life, self.wbc_life_rect)
     self.screen.blit(self.rank_image, self.rank_image_ract )