# -*- coding: utf-8 -*-
from kivy.graphics import Color
from kivy.input import MotionEvent
from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage

from .plotutil import *
from PIL.Image import Image as PilImage
import PIL


class QwtPainterWidget(Widget):
    """
        代表绘图的widget
    """

    # todo 如何实现撤销和重做功能

    # 绘图工具管理器
    _tool_manager: PlotToolManager

    # 当前绘图工具
    _cur_plot_tool: AbstractPlotTool = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._tool_manager = PlotToolManager(self)
        pass

    # todo 在 ubuntu 系统下，发现在程序失去焦点时，仍旧可以获得 触摸板的事件，导致绘图
    def on_touch_down(self, touch: MotionEvent) -> bool:
        if self._cur_plot_tool is None:
            return False
        return self._cur_plot_tool.on_touch_down(touch)

    def on_touch_move(self, touch) -> bool:
        if self._cur_plot_tool is None:
            return False
        return self._cur_plot_tool.on_touch_move(touch)

    def on_touch_up(self, touch) -> bool:
        if self._cur_plot_tool is None:
            return False
        return self._cur_plot_tool.on_touch_up(touch)

    def set_line_width(self, width: float):
        """
        设置线宽
        """
        self._tool_manager.set_line_width(width)
        pass

    def set_line_color(self, color: tuple):
        """
        设置线颜色
        """
        self._tool_manager.set_line_color(color)
        pass

    def set_tool_type(self, tool_type: PlotToolType):
        """
        设置绘图工具类型
        """
        self._cur_plot_tool = self._tool_manager.set_tool_type(tool_type)
        pass

    def get_paint_image(self) -> PilImage:
        """
        获取绘图结果, 并将其转换为 PIL.Image.Image 类型
        """
        # 1. 导出为 kivy core image
        core_image: CoreImage = self.export_as_image()
        print(PIL.Image.EXTENSION)
        return None