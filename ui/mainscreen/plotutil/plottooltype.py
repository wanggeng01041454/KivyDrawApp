# -*- coding: utf-8 -*-

from enum import Enum


class PlotToolType(Enum):
    """
    绘图类型
    """
    # 铅笔
    PENCIL = 1
    # 直线
    LINE = 2
    # 矩形
    RECTANGLE = 3
    # 椭圆
    ELLIPSE = 4
    # 橡皮擦
    ERASER = 5
