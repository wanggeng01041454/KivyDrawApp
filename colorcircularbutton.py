# -*- coding: utf-8 -*-

from kivy.graphics import Color, Ellipse
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.button import Button


class ColorCircularButton(Button):
    """
    显示一个颜色圆圈的 widget
    可以用来表示线型的粗细和颜色
    """

    """show_color属性: 表示颜色的 rgba 值"""
    show_color = ListProperty([0, 0, 0, 1])

    """width属性: 表示线宽"""
    show_width = NumericProperty(1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 绑定事件: 显示颜色和线宽改变时更新显示
        self.bind(show_color=self._update_property)
        self.bind(show_width=self._update_property)
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
            Color(*self.show_color)
            # d是圆的直径； 为了显示线宽，直径是线宽的两倍
            d = self.show_width*2
            # 画圆
            pos_x = self.center_x - d / 2
            pos_y = self.center_y - d / 2
            print("d={}, x={}, y={}".format(d, pos_x, pos_y))
            Ellipse(pos=(pos_x, pos_y), size=(d, d))
        pass

