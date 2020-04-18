import sys
import pygame
from bullet import Bullet
from ncov import nCoV
from pygame.sprite import Group
import random
from time import sleep
import sys
"""事件"""
def check_keydown_events(event,settings,screen,wbc,bullets,index):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动
        wbc.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动
        wbc.moving_left = True
    elif event.key == pygame.K_UP:
        # 向上移动
        wbc.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 向下移动
        wbc.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 根据index产生子弹类型
        settings.bullet_sound.play()
        fire_bullet(settings,screen,wbc,bullets,index+1,settings.bullet_life_list[index+1])

    elif event.key == pygame.K_b:
        fire_bullet(settings,screen,wbc,bullets,1,settings.bullet_life_list[1])
    elif event.key == pygame.K_v:
        fire_bullet(settings,screen,wbc,bullets,2,settings.bullet_life_list[2])
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,wbc):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        # 向右移动
        wbc.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向左移动
        wbc.moving_left = False
    elif event.key == pygame.K_UP:
        # 向上移动
        wbc.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 向下移动
        wbc.moving_down = False

def check_events(settings,screen,wbc,bullets,index):
    """响应按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings,screen,wbc,bullets,index)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,wbc)

"""绘制屏幕"""
def updata_screen(screen,settings,background,ncovs_list,wbc,bullets,sb,gifts):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # #每次循环时候重绘屏幕
    screen.blit(background, (0, 0))
    # 绘制红包
    gifts.draw(screen)
    # 绘制病毒
    for ncovs in ncovs_list:
        for ncov in ncovs.sprites():
            if ncov.life < 0:
                for i in range(0, 6):
                    settings.bomb_sound.play()
                    screen.blit(settings.bomb_image[i], ncov.rect)
                ncovs.remove(ncov)
            else:
                ncov.prep_life()
                ncov.blitme()
        # ncovs.draw(screen)

    # 绘制白细胞
    wbc.blitme_play(settings.wbc_image_path[settings.wbc_image_index])
    # wbc.blitme()
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示得分
    sb.show_score()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

"""创建，病毒，礼物，子弹"""
def create_fleet(settings, screen,stats):
    # 根据等级创建新的病毒
    ncovs_list = []

    # 三种病毒精灵组
    ncovs = Group()
    for i in range(stats.level):
        ncov = nCoV(settings, screen, img_path=settings.ncov_image_path[2],index=-1,stats=stats,life=settings.ncov_life_list[0],speed=0)
        ncovs.add(ncov)
    ncovs_list.append(ncovs)

    ncovs1 = Group()
    for i in range(stats.level*2):
        ncov = nCoV(settings, screen, img_path=settings.ncov_image_path[1],index=-1,stats=stats,life=settings.ncov_life_list[1],speed=1)
        ncovs1.add(ncov)
    ncovs_list.append(ncovs1)

    ncovs2 = Group()
    for i in range(stats.level * 3):
        ncov = nCoV(settings, screen, img_path=settings.ncov_image_path[0],index=-1,stats=stats,life=settings.ncov_life_list[2],speed=2)
        ncovs2.add(ncov)
    ncovs_list.append(ncovs2)
    return ncovs_list

def create_gift(settings, screen,gifts,stats):
    """生成礼物"""
    # 随机生成礼物属性
    index = random.randint(0,1)
    # 创建礼物
    ncov = nCoV(settings, screen, settings.gift_image_path[index],index,stats,life=1,speed=0)
    # 加入精灵组
    gifts.add(ncov)

def fire_bullet(settings,screen,wbc,bullets,img,life):
    """如果还没达到限制，就发射一颗子弹"""
    #创建新的子弹，并将其加入编组bullets中
    if img !=0 and len(bullets)>10:
        img =0
    if len(bullets) < 100:
        # 创建一颗子弹
        new_bullet = Bullet(settings, screen, wbc,img,life)
        # 并将其加入到班组bullets中
        bullets.add(new_bullet)


"""update 白细胞，病毒，子弹"""
def updata_wbc(wbc,ncovs_list,stats,screen,settings,sb):
    """白细胞移动"""
    # 白细胞移动
    wbc.update()
    for ncovs in ncovs_list:
        # 检测白细胞与病毒之间的碰撞,检测多种病毒与白细胞之间的碰撞
        if pygame.sprite.spritecollide(wbc, ncovs, True):
            # 白细胞生命减少
            settings.wbc_limit -=1
            # 如果生命晓雨0，游戏结束
            if settings.wbc_limit==0:
                stats.game_active = False
        # 病毒是否超过底端
        if check_ncovs_bottom(screen, ncovs,):
            settings.wbc_limit -= 1
            if settings.wbc_limit == 0:
                stats.game_active = False
        # for ncov in ncovs.sprites():
        #     # 如果病毒生命小于0，则删除他
        #     if ncov.life <= 0:
        #         draw_bomb(settings, screen, ncov)
        #         ncovs.remove(ncov)
        # 更新生命值
        sb.prep_wbcs()
        # 更新病毒位置
        updata_nocv(ncovs)

def updata_nocv(ncovs):
    """病毒移动"""
    for ncov in ncovs.sprites():
        ncov.update()

def updata_bullet(settings,bullets,ncovs_list,stats,sb):
    """子弹移动"""
    # 更新子弹位置
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for bullet in bullets.sprites():
        if bullet.life<=0:

            bullets.remove(bullet)
    # 检测子弹与病毒之间的碰撞
    for i in range(len(ncovs_list)):
        check_bullet_ncovs_collisions(settings, bullets, ncovs_list[i], stats,sb)
        # 如果病毒精灵组为空
        if len(ncovs_list[i]) == 0:
            k = i
        else:
            k =None
     # 删除病毒精灵组为空的精灵组
    if k != None:
        del ncovs_list[k]

"""碰撞检测-病毒与子弹，病毒是否到达底部"""
def check_bullet_ncovs_collisions(settings,bullets,ncovs,stats,sb):
    """检测子弹与病毒之间的碰撞"""
    # 删除碰撞的子弹与病毒
    collisions = pygame.sprite.groupcollide(bullets, ncovs, False, False, )
    # 根据collisions计算得分
    if collisions:
        for bullet in collisions.keys():
            bullet.life -= 1
        for ncovs in collisions.values():
            # 分数等于=基础分*发生碰撞的病毒个数
            stats.score += settings.ncov_points * len(ncovs)
            # 计算生命
            for ncov in ncovs:
                ncov.life -=1
            # 显示分数
            sb.prep_score()
            # 检查是否生成最高分
            check_high_score(stats, sb)

def check_ncovs_bottom(screen, ncovs,):
    """检查是否有病毒到达了屏幕底端"""
    # 获取屏幕rect
    screen_rect = screen.get_rect()
    for ncov in ncovs.sprites():
        # 如果病毒的底大于屏幕的底
        if ncov.rect.bottom >= screen_rect.bottom:
            # 删除该病毒
            ncovs.remove(ncov)
            # 暂停
            sleep(0.5)
            return True
    return False

def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

""""如果病毒被消灭"""

def reset(ncovs_list,bullets,stats,sb,settings,screen,gifts):
    # 渲染最高得分
    sb.prep_high_score()
    # 如果所有病毒都被消灭，就提高一个等级
    if len(ncovs_list) == 0:
        settings.win_sound.play()
        sleep(3)
        # 清空子弹
        bullets.empty()
        # 提高等级
        stats.level += 1
        # 如果等级大于10，则更新rank
        if stats.level%10 == 0 and stats.level/10>float(settings.rank_in):
            settings.rank_in = stats.level/10
            sb.prep_rank()
        sb.prep_level()
        # 更新速度
        settings.increase_speed()
        # 创建新的礼物
        create_gift(settings, screen, gifts,stats)
        # 创建新的病毒
        ncovs_list = create_fleet(settings, screen, stats)
        settings.index = -1

    return ncovs_list

def check_gifts(wbc,gifts):
    """检测红包和白细胞之间的碰撞,并返回其礼物种类"""
    collide_list = pygame.sprite.spritecollide(wbc, gifts, True)
    if collide_list:
        return collide_list[0].index

def end_time(screen):
    font = pygame.font.SysFont(None, 100)
    text_color = (30, 30, 30)
    bg_color = (230, 230, 230)
    screen_rect = screen.get_rect()
    for i in range(5, 1, -1):
        font_image = font.render("{0}".format(i), True, text_color, bg_color)
        font_rect = font_image.get_rect()
        font_rect.right = screen_rect.right - 480
        font_rect.top = 200
        screen.blit(font_image, font_rect)
        pygame.display.flip()
        sleep(1)
# def draw_bomb(settings,screen,ncov):
#     for i in range(0,6):
#         screen.blit(settings.bomb_image[i],ncov.rect)
#         # sleep(0.04)