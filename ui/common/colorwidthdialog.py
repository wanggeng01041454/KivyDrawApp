# -*- coding: utf-8 -*-

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDColorPicker
from kivymd.uix.slider import MDSlider

from colorwidthrepresentbutton import ColorWidthRepresentButton


class ColorWidthDialogContent(BoxLayout):
    """
    颜色和线宽选择对话框的显示内容
    """
    # 存放选择结果的按钮
    result_btn = ObjectProperty(None)

    def __int__(self, **kwargs):
        """
        构造函数
        :param kwargs:
        :return:
        """
        super().__int__(**kwargs)

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
        pass

    def open_color_picker(self, *args):
        """
        打开颜色选择器
        :return:
        """
        color_picker = MDColorPicker(
            size_hint=(0.45, 0.85),
            type_color="HEX",
        )
        color_picker.bind(on_release=self.get_picker_selected_color)
        color_picker.open()
        pass

    def get_picker_selected_color(
            self,
            instance_color_picker: MDColorPicker,
            type_color: str,
            selected_color: list,
    ):
        """
        获取颜色选择器的选择结果,
        用于绑定 MDColorPicker 的 on_release 事件
        :param instance_color_picker:
        :param type_color:
        :param selected_color: 查看了 MDColorPicker 的源码，发现 selected_color 总是是一个长度为4的列
        :return:
        """
        self.result_btn.represent_color = selected_color
        instance_color_picker.dismiss()
        pass


class ColorWidthDialog(MDDialog):
    """
    选择颜色和线宽的对话框
    """

    def __init__(self, **kwargs):
        """
        构造函数
        :param kwargs:
        """
        ok_btn = MDFlatButton(
            text="OK",
            theme_text_color="Custom"
        )
        # 将ok按钮的事件绑定到函数
        ok_btn.bind(on_release=self._release_ok_btn)
        # type, content_cls, buttons 必须放在构造函数中； 因为父类构造函数初始化时，需要它们的信息
        super().__init__(
            title="choose color and line width",
            type="custom",
            content_cls=ColorWidthDialogContent(),
            buttons=[ok_btn],
            **kwargs)
        # False时，点击空白处，不能自行关闭；True时，点击空白处可以自行关闭; 默认为True
        self.auto_dismiss = True
        # 注册事件
        self.register_event_type("on_ok_btn_release")
        pass

    def _release_ok_btn(self, *args):
        self.dismiss()
        # 事件分发
        self.dispatch(
            "on_ok_btn_release",
            self.content_cls.result_btn.represent_color,
            self.content_cls.result_btn.represent_width
        )
        pass

    def on_ok_btn_release(self, color: list, width: float):
        """
        定义事件函数
        ok按钮被点击(并释放后)调用该函数
        :param color:
        :param width:
        :return:
        """
        pass
