from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.colorpicker import ColorPicker
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.popup import Popup

from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from plotutil.plottooltype import PlotToolType
from qwtpainterwidget import QwtPainterWidget  # 解析 kv 文件时需要

from colorcircularbutton import ColorCircularButton


class Cpicker(ColorPicker):
    pass


class popup(Popup):
    def hello(self, y):
        global clr, pre_clr
        pre_clr = clr
        clr = y


class MainScreen(MDScreen):
    painter = ObjectProperty(None)
    color_button = ObjectProperty(None)
    ctn = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 设置默认状态
        self.painter.set_line_width(1.0)
        self.painter.set_tool_type(PlotToolType.PENCIL)
        self.painter.set_line_color((0, 0, 0, 1))

        pass

    def open_it1(self):
        # popup().open()
        self.ctn += 1
        print("ctn = ", self.ctn)
        if self.ctn % 2 == 0:
            self.color_button.show_color = [1, 0, 0, 1]
            self.ctn = 0
        else:
            self.color_button.show_color = [0, 1, 0, 1]
        pass

    def eraser(self):
        pass

    def on_width_change(self, width: float):
        """
        当宽度改变时调用
        :param width:
        :return:
        """
        # 根据实际使用经验，从界面得到的值有时会包含小数点后很多位，这里只保留1位小数
        width = round(width, 1)
        # self.lab.text = "Width : " + str(value)
        self.painter.set_line_width(width)
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
