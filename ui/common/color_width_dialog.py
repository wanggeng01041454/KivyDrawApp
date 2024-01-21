# -*- coding: utf-8 -*-

import os

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog

from .color_width_represent_button import ColorWidthRepresentButton

from ui import ui_common_path
from tools import ResourceManager
from .qwt_color_picker import QwtColorPicker

"""导出的类"""
__all__ = ['ColorWidthDialog']

# 在导入本文件时，打开build对应的kv文件
with open(
    os.path.join(ui_common_path, "color_width_dialog.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class ColorWidthDialogContent(BoxLayout):
    """
    颜色和线宽选择对话框的显示内容
    """
    # 展示选择结果的按钮
    result_btn: ColorWidthRepresentButton = ObjectProperty(None)
    color_picker: QwtColorPicker = None

    # 最终结果的颜色和线宽
    _color: list = None
    _width: float = None

    def __init__(self, **kwargs):
        """构造函数"""
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self._lazy_init(), 0)
        # 注册事件
        self.register_event_type("on_select")
        pass

    def _lazy_init(self):
        """延迟初始化"""
        self.color_picker = QwtColorPicker(
            size_hint=(0.6, 1),
        )
        # 绑定颜色选择器的选择颜色事件，每次在颜色选择器中选择颜色都会触发
        self.color_picker.bind(on_select_color=self._on_selected_color_receiver)
        self._color = self.result_btn.represent_color
        self._width = self.result_btn.represent_width
        pass

    def on_width_change(self, *args):
        """
        宽度变更
        :param args:
            args[0] 是 instance
            args[1] 是 value
        :return:
        """
        self.result_btn.represent_width = args[1]
        self._width = args[1]
        self._emit_event()
        pass

    def on_color_change(self, *args):
        """
        颜色变更, 取被点击按钮的颜色
        :param args:
            args 长度为1
            args[0] 是 instance
        :return:
        """
        btn: ColorWidthRepresentButton = args[0]
        self.result_btn.represent_color = btn.represent_color
        self._color = btn.represent_color
        self._emit_event()
        pass

    def open_color_picker(self, *args):
        """
        打开颜色选择器
        :return:
        """
        self.color_picker.open()
        pass

    def _on_selected_color_receiver(
            self,
            instance_color_picker: QwtColorPicker,
            color: list,
    ):
        """
        on_select_color的事件接收器
        用于绑定 color_picker 的 on_release 事件
        :param instance_color_picker:
        :param color: 被选中的颜色，是一个 rgba 列表
        :return:
        """
        self.result_btn.represent_color = color
        self._color = color
        self._emit_event()
        pass

    def _emit_event(self):
        """发射事件"""
        self.dispatch("on_select", self._color, self._width)
        pass

    def on_select(self, color: list, width: float):
        """
        选定颜色和线宽时，发射该事件
        :param color:
        :param width:
        :return:
        """
        pass

    pass


class ColorWidthDialog(MDDialog):
    """
    选择颜色和线宽的对话框，用于选择画笔颜色和线宽
    在选择颜色和线宽后，会发射 on_select 事件
    """

    def __init__(self, **kwargs):
        """
        构造函数
        :param kwargs:
        """
        res_mgr = ResourceManager()
        # type, content_cls, buttons 必须放在构造函数中； 因为父类构造函数初始化时，需要它们的信息
        color_width_dlg_content = ColorWidthDialogContent()
        super().__init__(
            title=res_mgr.get_lang_text('main_screen', 'color_dlg_title', embed_font=True),
            type="custom",
            content_cls=color_width_dlg_content,
            **kwargs)
        # False时，点击空白处，不能自行关闭；True时，点击空白处可以自行关闭; 默认为True
        self.auto_dismiss = True
        color_width_dlg_content.bind(on_select=self._on_select_receiver)
        # 注册事件
        self.register_event_type("on_select")
        pass

    def _on_select_receiver(self, instance: ColorWidthDialogContent, color: list, width: float):
        # 事件分发
        self.dispatch(
            "on_select",
            self.content_cls.result_btn.represent_color,
            self.content_cls.result_btn.represent_width
        )
        pass

    def on_select(self, color: list, width: float):
        """
        当选定颜色和线宽时，发射该事件
        ok按钮被点击(并释放后)调用该函数
        :param color:
        :param width:
        :return:
        """
        pass
