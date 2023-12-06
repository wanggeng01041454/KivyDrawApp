# -*- coding: utf-8 -*-
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDColorPicker
from kivymd.uix.slider import MDSlider

from colorcircularbutton import ColorCircularButton


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
        ok_btn.bind(on_press=self._click_ok_btn)
        # type, content_cls, buttons 必须放在构造函数中； 因为父类构造函数初始化时，需要它们的信息
        super().__init__(
            title="choose color and line width",
            type="custom",
            content_cls=ColorWidthDialogContent(),
            buttons=[ok_btn],
            **kwargs)
        # False时，点击空白处，不能自行关闭；True时，点击空白处可以自行关闭; 默认为True
        self.auto_dismiss = True
        pass

    def _click_ok_btn(self, *args):
        self.dismiss()
        pass

