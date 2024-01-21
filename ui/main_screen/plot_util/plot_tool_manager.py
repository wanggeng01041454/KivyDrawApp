# -*- coding: utf-8 -*-
from kivy.uix.widget import Widget

from ui.main_screen.plot_util.abstract_plot_tool import AbstractPlotTool
from ui.main_screen.plot_util.line_tool import LineTool
from ui.main_screen.plot_util.pencil_tool import PencilTool
from ui.main_screen.plot_util.plot_tool_type import PlotToolType
from ui.main_screen.plot_util.rectangle_tool import RectangleTool


class PlotToolManager:
    """
    绘图工具管理器
    """

    # 线宽
    _line_width: float = 1.0

    # 当前绘图工具类型
    _current_tool_type: PlotToolType = None

    # 当前绘图颜色
    _current_color: tuple = (1, 1, 1, 1)

    # 绘图工具类型到绘图工具的映射
    _type2tool: dict

    def __init__(self, tool_parent: Widget):
        self._type2tool = dict()
        self._type2tool[PlotToolType.PENCIL] = PencilTool(tool_parent)
        self._type2tool[PlotToolType.LINE] = LineTool(tool_parent)
        self._type2tool[PlotToolType.RECTANGLE] = RectangleTool(tool_parent)
        pass

    def set_line_width(self, width: float):
        """
        设置线宽
        """
        self._line_width = width
        if self._current_tool_type is not None:
            self._type2tool[self._current_tool_type].set_line_width(width)
        pass

    def set_line_color(self, color: tuple):
        """
        设置线颜色
        """
        self._current_color = color
        if self._current_tool_type is not None:
            self._type2tool[self._current_tool_type].set_line_color(color)
        pass

    def set_tool_type(self, tool_type: PlotToolType) -> AbstractPlotTool:
        """
        设置绘图工具类型, 返回当前绘图工具
        """
        if tool_type not in self._type2tool:
            raise ValueError("tool_type is not implemented")

        self._current_tool_type = tool_type

        # 为当前选中的工具设置线宽和颜色
        self._type2tool[tool_type].set_line_width(self._line_width)
        self._type2tool[tool_type].set_line_color(self._current_color)

        return self._type2tool[tool_type]


