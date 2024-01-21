# -*- coding: utf-8 -*-

from kivy.graphics import Color, Line
from kivy.input import MotionEvent
from kivy.uix.widget import Widget

from ui.main_screen.plot_util.abstract_plot_tool import AbstractPlotTool


class LineTool(AbstractPlotTool):
    """
    直线工具
    """

    # 绘图起始位置
    _start_pos_x: float = 0.0
    _start_pos_y: float = 0.0

    # 是否开始了绘图， 是否接收到到过 touch down 事件
    _start = False

    def __init__(self, parent: Widget):
        super().__init__(parent)

    def _reset(self):
        """
        重置
        """
        self._start_pos_x = 0.0
        self._start_pos_y = 0.0
        self._start = False
        pass

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """
        touch down 事件
        """
        if not self._is_in_canvas(touch):
            return False

        self._start_pos_x = touch.x
        self._start_pos_y = touch.y
        self._start = True
        return True

    def on_touch_move(self, touch: MotionEvent) -> bool:
        """
        touch move 事件
        """
        if not self._is_in_canvas(touch):
            return False
        if not self._start:
            return False

        self._parent.canvas.after.clear()
        with self._parent.canvas.after:
            Color(*self._line_color)
            Line(points=(self._start_pos_x, self._start_pos_y, touch.x, touch.y), width=self._line_width)

        return True

    def on_touch_up(self, touch: MotionEvent) -> bool:
        """
        touch up 事件
        """
        if not self._is_in_canvas(touch):
            return False
        if not self._start:
            return False

        self._parent.canvas.after.clear()
        with self._parent.canvas:
            Color(*self._line_color)
            Line(points=(self._start_pos_x, self._start_pos_y, touch.x, touch.y), width=self._line_width)

        # 触摸结束，重置状态
        self._reset()

        return True
