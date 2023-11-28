from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.colorpicker import ColorPicker
from kivy.properties import ListProperty
from kivy.uix.popup import Popup

from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen

from plotutil.plottooltype import PlotToolType
from qwtpainterwidget import QwtPainterWidget  # 解析 kv 文件时需要


class Cpicker(ColorPicker):
    pass


class popup(Popup):
    def hello(self, y):
        global clr, pre_clr
        pre_clr = clr
        clr = y


class MainScreen(MDScreen):

    def open_it1(self):
        popup().open()

    def set_default_state(self):
        """
        设置默认状态
        :return:
        """

        self.painter.set_line_width(1.0)
        self.painter.set_tool_type(PlotToolType.PENCIL)
        self.painter.set_line_color((0, 0, 0, 1))
        pass


    def eraser(self):
        pass

    def on_width_change(self, value: float):
        """
        当宽度改变时调用
        :param value:
        :return:
        """
        # 根据实际使用经验，从界面得到的值有时会包含小数点后很多位，这里只保留1位小数
        value = round(value, 1)
        self.lab.text = "Width : " + str(value)
        self.painter.set_line_width(value)
        pass

    def on_select_pencil(self):
        """
        选择铅笔工具
        :return:
        """
        self.painter.set_tool_type(PlotToolType.PENCIL)
        pass

    def sl(self):
        pass

    def on_select_rect(self):
        """
        选择矩形工具
        :return:
        """
        self.painter.set_tool_type(PlotToolType.RECTANGLE)
