import pygame

class Ship():
    def __init__(self, ai_settings, screen): #初始化飞船并设置初始位置
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/ship.bmp') #加载图像
        self.rect = self.image.get_rect() #获取矩形形状
        self.screen_rect = screen.get_rect() #表示屏幕的矩形

        self.rect.centerx = self.screen_rect.centerx #飞船中心x坐标设置为表示屏幕的矩阵的属性
        self.rect.bottom = self.screen_rect.bottom #飞船底部y坐标设置为表示屏幕的矩阵的属性（pygame将使用这些rect属性）

        self.center = float(self.rect.centerx) #在飞船的属性center中存储小数值(rect属性只能为整数值)
        
        self.moving_right = False #移动标志
        self.moving_left = False

    def update(self): #根据移动标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center #更新rect

    def blitme(self): #在指定位置绘制
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船居中"""
        self.center = self.screen_rect.centerx