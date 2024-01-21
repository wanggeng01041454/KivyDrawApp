# -*- coding: utf-8 -*-
from kivy.input import MotionEvent
from kivy.uix.widget import Widget


class AbstractPlotTool:
    """
    绘图工具的抽象基类
    """

    # 代表绘图工具的父对象，绘图在其上完成
    _parent: Widget

    # 线宽
    _line_width: float

    # 当前绘图颜色
    _line_color: tuple

    def __init__(self, parent: Widget):
        self._parent = parent
        pass

    def set_line_width(self, width: float):
        """
        设置线宽
        """
        self._line_width = width
        pass

    def set_line_color(self, color: tuple):
        """
        设置线颜色
        """
        self._line_color = color
        pass

    def _is_in_canvas(self, touch: MotionEvent) -> bool:
        """
        判断触摸点是否在父对象的画布内
        """
        x = touch.x - self._parent.x
        y = touch.y - self._parent.y

        if 0 < x < self._parent.width and 0 < y < self._parent.height:
            return True
        else:
            return False

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """
        touch down 事件
        """
        return False

    def on_touch_move(self, touch: MotionEvent) -> bool:
        """
        touch move 事件
        """
        return False

    def on_touch_up(self, touch: MotionEvent) -> bool:
        """
        touch up 事件
        """
        return False