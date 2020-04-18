import pygame
class Settings():
    """储存的所有类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 536
        self.bg_image_path = r'resplane\image\background_wzd.png'
        self.bg_login_mage_path = r'resplane\image\background_img.png'
        self.bg_color = (230, 230, 230)

        """"排名段位 """
        self.rank_in = float(0)
        self.rank_in_images_path = []
        for i in range(0,8):
            self.rank_in_images_path.append(r'resplane\image\r{0}.png'.format(i))

        """病毒基础设置"""
        self.ncov_image_index = 0
        self.ncov_image_path = []
        for i in range(60,63):
            self.ncov_image_path.append(r'resplane\image\{0}.png'.format(i))
        # 速度
        self.ncov_speed = 2
        self.ncov_speed_list = [self.ncov_speed, self.ncov_speed/2, self.ncov_speed/4]
        # 记分
        self.ncov_points = 1
        # 病毒生命
        self.ncov_life_base =1
        self.ncov_life_list=[self.ncov_life_base,self.ncov_life_base*5,self.ncov_life_base*10]

        # 礼物基础设置
        self.gift_image_index = 0
        self.gift_image_path = []
        for i in range(1, 3):
            self.gift_image_path.append(r'resplane\image\红包{0}.png'.format(i))

        """白细胞基础设置"""
        self.wbc_image_index = 0
        self.wbc_image_path = []
        for i in range(1,7):
            self.wbc_image_path.append(r'resplane\image\b_{0}.png'.format(i))
        # 速度
        self.wbc_speed = 20
        # 白细胞生命
        self.wbc_limit = 10



        """子弹类设置 """
        self.index = -1
        self.bullet_image_path = []
        for i in range(1, 4):
            self.bullet_image_path.append(r'resplane\image\子弹{0}.png'.format(i))
        # 子弹基础速度
        self.bullet_base_speed = 20
        # 子弹速度列表
        self.bullet_speed_list = [self.bullet_base_speed,self.bullet_base_speed/5,self.bullet_base_speed*5]

        # 子弹基础生命
        self.bullet_life_base=5
        # 子弹速度列表
        self.bullet_life_list=[self.bullet_life_base,self.bullet_life_base*20,self.bullet_life_base*4]


        # 爆炸
        self.bomb_image = []
        for i in range(0, 6):
            self.bomb_image.append(pygame.image.load(r'resplane\image\{0}.png'.format(i)))

        self.initialize_dynamic_settings()
        self.speedup_scale = 1.1

        """声音"""
        self.bullet_sound = pygame.mixer.Sound(r'resplane\sound\bullet.wav')
        self.bullet_sound.set_volume(1)
        self.bomb_sound = pygame.mixer.Sound(r'resplane\sound\enemy2_down.wav')
        self.win_sound = pygame.mixer.Sound(r'resplane\sound\win_music.wav')
        self.death_sound = pygame.mixer.Sound(r'resplane\sound\death.wav')
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 根据段位增加游戏难度
        rank= 1+(0.1*float(self.rank_in))
        self.ncov_speed = 2*float(rank)
        self.wbc_speed = 20*float(rank)
        self.bullet_base_speed = 20*float(rank)

    def increase_speed(self):
        """提高速度设置"""
        self.wbc_speed *= self.speedup_scale

        # 子弹速度
        self.bullet_base_speed *= self.speedup_scale
        self.bullet_speed_list = [self.bullet_base_speed, self.bullet_base_speed / 5, self.bullet_base_speed * 5]
        # 子弹生命
        self.bullet_life_base *= 2
        self.bullet_life_list = [self.bullet_life_base, self.bullet_life_base * 500, self.bullet_life_base * 4]

        # 病毒生命
        self.ncov_life_base *= 2
        self.ncov_life_list = [self.ncov_life_base, self.ncov_life_base * 2, self.ncov_life_base * 4]
        # 病毒速度
        self.ncov_speed *= self.speedup_scale
        self.ncov_speed_list = [self.ncov_speed, self.ncov_speed *1.2, self.ncov_speed *1.1]