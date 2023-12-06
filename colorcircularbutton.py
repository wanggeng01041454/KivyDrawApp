# -*- coding: utf-8 -*-

from kivy.graphics import Color, Ellipse, Line
from kivy.properties import ListProperty, NumericProperty, BooleanProperty
from kivy.uix.button import Button


class ColorCircularButton(Button):
    """
    显示一个颜色圆圈的 widget
    可以用来表示线型的粗细和颜色
    """

    """represent_color 属性: 所代表的颜色的 rgba 值"""
    represent_color = ListProperty([0, 0, 0, 1])

    """represent_width 属性: 所代表的线宽"""
    represent_width = NumericProperty(5.0)

    """是否显示边框, 默认是显示的"""
    display_border = BooleanProperty(True)

    def __init__(self, **kwargs):
        """
        构造函数
        """
        super().__init__(**kwargs)

        # 绑定事件: 显示颜色和线宽改变时更新显示
        self.bind(represent_color=self._update_property)
        self.bind(represent_width=self._update_property)
        self.bind(display_border=self._update_property)
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
            # todo 如果在手机和windows上显示的圆也不好的话，就换成正方形
            # d是圆的直径； 为了显示线宽，直径是线宽的两倍
            d = self.represent_width
            # 画填充圆
            pos_x = self.center_x - d / 2
            pos_y = self.center_y - d / 2
            Ellipse(pos=(pos_x, pos_y), size=(d, d))

            # 画边框
            if self.display_border:
                circle_radius = min(self.width, self.height) / 2
                Line(circle=(self.center_x, self.center_y, circle_radius), width=1.0)
        pass

