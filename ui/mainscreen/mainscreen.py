# -*- coding: utf-8 -*-

from kivy.properties import ObjectProperty

from kivymd.uix.screen import MDScreen

from .plotutil import PlotToolType

from ui.common import ColorWidthDialog
from ui.common import MDIconHoverButton

from .promptdialog import PromptDialog
# 引用这个类，是为了在 kv 文件中使用这个类
from .qwtpainterwidget import QwtPainterWidget


class MainScreen(MDScreen):
    """
    主界面
    """
    """绘图板"""
    painter = ObjectProperty(None)
    """展示颜色和线条宽度的按钮"""
    color_button = ObjectProperty(None)
    """颜色和线条宽度选择对话框"""
    color_width_dialog: ColorWidthDialog = None

    """当前被选中的 hover 按钮"""
    cur_selected_hover_button: MDIconHoverButton = None

    """提示词对话框"""
    prompt_dialog: PromptDialog = None

    def __init__(self, **kwargs):
        """
        构造函数
        todo 在构造函数中调用 set_cur_selected_hover_button 设置初始选中的按钮，会导致一些异常：
        todo 包括: 在 is 比较时失效， 按钮的图标大小无法恢复等
        """
        super().__init__(**kwargs)
        # 设置默认状态, 使用pencil工具
        default_width = 3.0
        default_color = [0, 0, 0, 1]
        self.painter.set_line_width(default_width)
        self.painter.set_line_color(default_color)
        self.color_button.represent_color = default_color
        self.color_button.represent_width = default_width
        # 创建颜色和宽度选择对话框
        self.color_width_dialog = ColorWidthDialog()
        # 绑定颜色和宽度选择对话框的 ok 按钮事件
        self.color_width_dialog.bind(on_ok_btn_release=self.on_color_width_dialog_ok_btn_release)

        # 创建提示词对话框
        self.prompt_dialog = PromptDialog()
        pass

    def on_show_prompt_dialog(self, *args):
        """
        显示提示词对话框
        :param args:
        :return:
        """
        self.prompt_dialog.open()
        pass

    def on_ai_process(self, *args):
        """
        AI处理
        :param args:
        :return:
        """
        # todo AI处理
        self.painter.get_paint_image()
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

    def on_select_pencil(self, *args):
        """
        选择铅笔工具
        :return:
        """
        self.painter.set_tool_type(PlotToolType.PENCIL)
        self.set_cur_selected_hover_button(args[0])
        pass

    def on_select_line(self, *args):
        """
        选择直线工具
        :return:
        """
        self.painter.set_tool_type(PlotToolType.LINE)
        self.set_cur_selected_hover_button(args[0])
        pass

    def on_select_rect(self, *args):
        """
        选择矩形工具
        :return:
        """
        self.painter.set_tool_type(PlotToolType.RECTANGLE)
        self.set_cur_selected_hover_button(args[0])
        pass

    def on_select_eraser(self, *args):
        """
        选择橡皮擦工具
        :param args:
        :return:
        """
        pass

    def on_clear_canvas(self, *args):
        """
        清空画布
        清空画布时，不修改当前选中的 hover 按钮
        :param args:
        :return:
        """
        self.painter.canvas.clear()
        self.painter.canvas.after.clear()
        pass

    def set_cur_selected_hover_button(self, button: MDIconHoverButton):
        """
        设置当前被选中的 hover 按钮，
        需要清除之前按钮的选中状态，并设置新按钮的选中状态
        :param button:
        :return:
        """
        # 清除之前按钮的选中状态
        if self.cur_selected_hover_button is not None:
            self.cur_selected_hover_button.set_normal_state()
        # 设置新按钮的选中状态，如果新按钮是 None，则不设置
        self.cur_selected_hover_button = button
        if self.cur_selected_hover_button is not None:
            self.cur_selected_hover_button.set_selected_state()
        pass

    def on_mouse_enter_button(self, *args):
        """
        鼠标进入按钮时调用，如果鼠标不是选中按钮，则设置按钮的 hover 状态
        :param args:
        :return:
        """
        button: MDIconHoverButton = args[0]
        if button is not self.cur_selected_hover_button:
            button.set_hover_state()
        pass

    def on_mouse_leave_button(self, *args):
        """
        鼠标离开按钮时调用，如果鼠标不是选中按钮，则设置按钮的 normal 状态
        :param args:
        :return:
        """
        button: MDIconHoverButton = args[0]
        if button is not self.cur_selected_hover_button:
            button.set_normal_state()
        pass
