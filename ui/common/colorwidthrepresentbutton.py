# -*- coding: utf-8 -*-

from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import ListProperty, NumericProperty, OptionProperty
from kivy.uix.button import Button

from .curve import normalized_curve_points


class ColorWidthRepresentButton(Button):
    """
    显示一个带颜色的圆，或者正方形，或者有宽带的线
    可以用来表示线型的粗细和颜色
    """

    """represent_color 属性: 所代表的颜色的 rgba 值"""
    represent_color = ListProperty([0, 0, 0, 1])

    """represent_width 属性: 所代表的线宽"""
    represent_width = NumericProperty(5.0)

    """显示类型: circle, square, line, curve， 默认是 circle"""
    display_type = OptionProperty("circle", options=["circle", "square", "line", "curve"])

    def __init__(self, **kwargs):
        """
        构造函数
        """
        super().__init__(**kwargs)

        # 绑定事件: 显示颜色和线宽改变时更新显示
        self.bind(represent_color=self._update_property)
        self.bind(represent_width=self._update_property)
        self.bind(display_type=self._update_property)
        # 中心点改变时更新显示
        self.bind(center_x=self._update_property)
        self.bind(center_y=self._update_property)
        pass

    def _update_property(self, *args):
        """
        更新属性
        """
        self.canvas.clear()
        with self.canvas:
            Color(*self.represent_color)

            if self.display_type == "circle":
                # 画填充圆
                d = self.represent_width  # 直径
                pos_x = self.center_x - d / 2
                pos_y = self.center_y - d / 2
                Ellipse(pos=(pos_x, pos_y), size=(d, d))
            elif self.display_type == "square":
                # 画填充正方形
                d = self.represent_width
                pos_x = self.center_x - d / 2
                pos_y = self.center_y - d / 2
                Rectangle(pos=(pos_x, pos_y), size=(d, d))
            elif self.display_type == "line":
                # 在中心划线, 线长为按钮宽度的 2/3
                pos_y = self.center_y
                begin_pos_x = self.center_x - self.width/3
                end_pos_x = self.center_x + self.width/3
                Line(points=(begin_pos_x, pos_y, end_pos_x, pos_y), width=self.represent_width)
            elif self.display_type == "curve":
                points = []
                for x, y in normalized_curve_points:
                    points.append(self.x + x*self.width)
                    points.append(self.y + y*self.height)
                Line(points=points, width=self.represent_width)
        pass

