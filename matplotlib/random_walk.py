from random import choice


class RandomWalk():
    """一个生成随机漫步的类"""
    def __init__(self, num_points=500):
        self.num_points = num_points

        # 所有随机漫步都开始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """获取步数"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """计算随机漫步的所有点"""

        while len(self.x_values) < self.num_points:

            # 决定前进方向和距离

            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原理踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

