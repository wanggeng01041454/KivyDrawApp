from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.properties import ListProperty, ObjectProperty


from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from plotutil.plottooltype import PlotToolType
from qwtpainterwidget import QwtPainterWidget  # 解析 kv 文件时需要

from colorwidthrepresentbutton import ColorWidthRepresentButton
from colorwidthdialog import ColorWidthDialog


class MainScreen(MDScreen):
    painter = ObjectProperty(None)
    color_button = ObjectProperty(None)
    color_width_dialog: ColorWidthDialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 设置默认状态
        default_width = 3.0
        default_color = [0, 0, 0, 1]
        self.painter.set_tool_type(PlotToolType.PENCIL)
        self.painter.set_line_width(default_width)
        self.painter.set_line_color(default_color)
        self.color_button.represent_color = default_color
        self.color_button.represent_width = default_width

        self.color_width_dialog = ColorWidthDialog()
        # 绑定事件
        self.color_width_dialog.bind(on_ok_btn_release=self.on_color_width_dialog_ok_btn_release)
        pass

    def open_color_width_dialog(self):
        self.color_width_dialog.open()
        pass

    def on_color_width_dialog_ok_btn_release(self, instance: ColorWidthDialog, color: list, width: float):
        self.color_button.represent_color = color
        self.painter.set_line_color(color)
        self.color_button.represent_width = width
        self.painter.set_line_width(width)
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
