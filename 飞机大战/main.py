"""
author:魏振东
date:20200407
func:planegame
"""
import pygame
from settings import Settings
from wbc import Wbc
from pygame.sprite import Group
import game_fun as gf
from game_stats import GameStats
from scoreboard import Scoreboard
import easygui as g
import pymysql_gui as pmsg
import sys
def rungame(score,rank_in,play):
    pygame.mixer.init()
    """类的实例"""
    # 基本设置类
    settings = Settings()
    # 子弹编组
    bullets = Group()
    # 礼包
    gifts = Group()

    # 统计游戏信息
    stats = GameStats(settings)

    """初始化 pygame"""

    pygame.init()
    # 设置游戏界面大小、背景图片及标题
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # 游戏界面标题
    pygame.display.set_caption('飞机大战')
    # 背景图
    background = pygame.image.load(settings.bg_image_path)
    # 初始化个人最高分
    stats.high_score = score
    # 初始化个人段位
    settings.rank_in = rank_in
    # 初始化个人基础速度
    settings.initialize_dynamic_settings()
    # 计分板
    sb = Scoreboard(settings, screen, stats)

    # 游戏循环帧率设置
    clock = pygame.time.Clock()
    wbc_list =[]
    # 白细胞类
    wbc = Wbc(settings, screen)
    wbc_list.append(wbc)
    if play == 2:
        wbc1 = Wbc(settings, screen)
        wbc_list.append(wbc1)

    # 创建一组病毒
    ncovs_list = gf.create_fleet(settings, screen, stats)
    # 倒计时
    gf.end_time(screen)
    """声音"""
    # pygame.mixer_music.load(r"resplane\sound\bgm4.mp3")
    # pygame.mixer_music.set_volume(0.2)
    # pygame.mixer_music.play()
    # 游戏主循环
    while True:
        if stats.game_active:
            # 监听事件
            gf.check_events(settings,screen,wbc_list,bullets,settings.index,)
            # 控制游戏最大帧率为 30
            clock.tick(30)
            # 更新白细胞位置，并对其进行与礼物和病毒的碰撞检测
            gf.updata_wbc(wbc_list,ncovs_list,stats,screen,settings,sb)
            # 检测白细胞与礼物之间的碰撞，index礼物编号
            for wbc in wbc_list:
                collide_list = pygame.sprite.spritecollide(wbc, gifts, True)
                if collide_list:
                    settings.index = collide_list[0].index
            # 更新子弹位置，并对其进行与病毒的碰撞检测
            gf.updata_bullet(settings,bullets,ncovs_list,stats,sb)
            # 更新礼物位置
            gf.updata_nocv(gifts)
            # 如果所有病毒都被消灭，就重置一些信息
            ncovs_list= gf.reset(ncovs_list, bullets, stats, sb, settings, screen, gifts)
            # 更新屏幕
            gf.updata_screen(screen,settings,background,ncovs_list,wbc_list,bullets,sb,gifts)
        else:
            print("游戏结束")
            settings.death_sound.play()
            return stats.high_score,settings.rank_in
# 登录
def login(title):
    msg = "请输入用户名和密码"
    title1 = "用户登录"
    user_info = g.multpasswordbox(msg,title1, ("用户名", "密码"))
    try:
        user = pmsg.select_mysql(user_info[0])
        # 验证数据库，密码
        if user_info[0] == user[1] and user_info[1] == user[2]:
            g.msgbox("登录成功！",title)
            while True:
                player = pmsg.select_mysql_by_id(user[0])
                # 基础排位信息
                if player[4] != None:
                    rank_in = player[4]
                # 个人最高得分
                if player[3] != None:
                    score = int(player[3])
                # 游戏开始 score最高分，rank_in排名段位
                high_score,rank = rungame(score,rank_in)
                print(pmsg.update_mysql(user[0],high_score,rank))
                choices = g.buttonbox(msg="游戏失败是否重新开始？",choices=("重新开始", "退出"))
                if choices == "重新开始":
                    pass
                elif choices == "退出":
                    sys.exit(0)
                else:
                    sys.exit(0)
        else:
            g.msgbox("账号或者密码错误，登录失败！请重新输入",title)
            login(title)
    except:
        msg = "游戏异常，是否退出？"
        choices = g.buttonbox(msg, choices=("登录","退出", ), title=title)
        if choices == "登录":
            login(title)
        elif choices == "退出":
            sys.exit(0)
        else:
            sys.exit(0)

# 注册
def register(title,):
    msg = "请输入用户名和密码"
    title1 = "注册"
    user_info = g.multpasswordbox(msg, title1, ("用户名", "密码"))
    # 验证账号是否已被注册
    try:
        if pmsg.insert_mysql(user_info[0],user_info[1]):
            g.msgbox("注册成功！",title)
            login(title)
        else:
            g.msgbox("注册失败！",title)
            register(title,)
    except:
        msg = "注册异常！！！是否退出？"
        choices = g.buttonbox(msg, choices=("注册", "退出",), title=title)
        if choices == "注册":
            register(title)
        elif choices == "退出":
            sys.exit(0)
        else:
            sys.exit(0)

if __name__ == '__main__':
    title = "飞机大战游戏"
    image = r'resplane\image\background_img.png'
    choices = g.buttonbox(image=image,choices=("登录", "注册","游客","游客双人"), title=title)
    if choices == "登录":
        login(title,)
    elif choices == "注册":
        register(title,)
    elif choices == "游客":
        while True:
            # 启动游戏
            high_score, rank = rungame(0, 0,1)
            choices = g.buttonbox(msg="游戏失败是否重新开始？", choices=("重新开始", "退出"))
            if choices == "重新开始":
                pass
            elif choices == "退出":
                sys.exit(0)
            else:
                sys.exit(0)
    elif choices == "游客双人":
        while True:
            # 启动游戏
            high_score, rank = rungame(0, 0,2)
            choices = g.buttonbox(msg="游戏失败是否重新开始？", choices=("重新开始", "退出"))
            if choices == "重新开始":
                pass
            elif choices == "退出":
                sys.exit(0)
            else:
                sys.exit(0)
    else:
        sys.exit(0)
