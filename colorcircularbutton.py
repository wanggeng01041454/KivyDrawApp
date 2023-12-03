# -*- coding: utf-8 -*-

from kivy.graphics import Color
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.button import Button


class ColorCircularButton(Button):
    """
    显示一个颜色圆圈的 widget
    可以用来表示线型的粗细和颜色
    """

    """color属性: 表示颜色的 rgba 值"""
    color = ListProperty([0, 0, 0, 1])

    """width属性: 表示线宽"""
    width = NumericProperty(1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # todo 搞清楚怎使用bind进行画图
        pass
