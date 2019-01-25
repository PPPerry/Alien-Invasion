import sys
import pygame
from pygame.sprite import Group
import os
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreborad

def run_game(): #初始化游戏
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings) #创建一个用于存储统计信息的实例
    sb = Scoreborad(ai_settings, screen, stats) #计分
    ship = Ship(ai_settings, screen) #创建一艘飞船
    aliens = Group() #创建一个外星人编组
    bullets = Group() #创建一个子弹编组

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True: #开始游戏的主循环

        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
 
run_game()

