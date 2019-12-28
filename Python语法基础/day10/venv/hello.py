"""
GUI
"""

# import tkinter
# import tkinter.messagebox
#
# def main():
#     flag = True
#
#     def change_label_text():
#         global flag
#         nonlocal flag
#         flag = not flag
#         color, msg = ("red", "hello") \
#             if flag else ("blue", "goodbye")
#         label.config(text=msg, fg=color)
#
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel("温馨提示", "quit？"):
#             top.quit()
#
#     top = tkinter.Tk()
#     top.geometry("240x160")
#     top.title("小游戏")
#     label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
#     label.pack(expand=1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
#     button1 = tkinter.Button(panel, text='修改', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()
# if __name__ == '__main__':
#     main()

"""
pygame
"""

from enum import Enum, unique
from math import sqrt
from random import randint

import pygame

@unique
class Color(Enum):
    """颜色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其它球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius += int(other.radius * 0.146)

    def draw(self, screen):
        """绘制"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)

def main():
    # 装所有的球
    balls = []
    # 初始化
    pygame.init()
    # 设置窗口
    screen = pygame.display.set_mode((800, 600))
    # 设置窗口标题
    pygame.display.set_caption("打球吃小球")

    running = True

    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获取点击鼠标位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)

        screen.fill((255, 255, 255))

        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        # 刷新
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main()


