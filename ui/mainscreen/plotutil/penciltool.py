# -*- coding: utf-8 -*-
from kivy.graphics import Color, Line
from kivy.input import MotionEvent
from kivy.uix.widget import Widget

from ui.mainscreen.plotutil.abstractplottool import AbstractPlotTool


class PencilTool(AbstractPlotTool):
    """
    铅笔工具
    """

    # 是否开始了绘图， 是否接收到到过 touch down 事件
    _start = False

    def __init__(self, parent: Widget):
        super().__init__(parent)

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """
        touch down 事件
        """
        if not self._is_in_canvas(touch):
            return False

        self._start = True
        with self._parent.canvas:
            Color(*self._line_color)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self._line_width)
        return True

    def on_touch_move(self, touch: MotionEvent) -> bool:
        """
        touch move 事件
        """
        if not self._is_in_canvas(touch):
            return False
        if not self._start:
            return False

        with self._parent.canvas:
            Color(*self._line_color)
            touch.ud['line'].points += [touch.x, touch.y]

        return True

    def on_touch_up(self, touch: MotionEvent) -> bool:
        """
        touch up 事件
        """
        if not self._is_in_canvas(touch):
            return False
        if not self._start:
            return False

        with self._parent.canvas:
            Color(*self._line_color)
            touch.ud['line'].points += [touch.x, touch.y]

        # 触摸结束，重置状态
        self._start = False

        return True

