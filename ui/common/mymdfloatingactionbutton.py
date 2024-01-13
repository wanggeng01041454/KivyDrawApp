# -*- coding: utf-8 -*-
from kivy.clock import Clock
from kivymd.uix.button import MDFloatingActionButton

from appconfig import BtnDingSound

black_color = [0, 0, 0, 1]
white_color = [1, 1, 1, 1]


class MyMDFloatingActionButton(MDFloatingActionButton):

    """
    自定义的 MDFloatingActionButton
    说明：虽然 MDFloatingActionButton 在 ubuntu 上显示不好看，但是在 android 上显示还是可以的
    """
    def __init__(self, **kwargs):
        """
        构造函数，初始化为默状态
        :param kwargs:
        """
        super().__init__(
            icon_size=64,
            **kwargs,
        )
        Clock.schedule_once(lambda dt: self.set_normal_state(), 0)
        pass

    def set_normal_state(self):
        """
        设置正常状态
        :return:
        """
        self.icon_color = black_color
        self.md_bg_color = "6296ea"  # CornFlowerBlue
        pass

    def set_selected_state(self):
        """
        设置被选中状态
        :return:
        """
        self.icon_color = white_color
        self.md_bg_color = "002afc"  # Blue

    def on_press(self, *args):
        BtnDingSound.play()
        return super().on_press(*args)
    # def on_touch_down(self, touch):
    #     """
    #     重写 on_touch_down 方法
    #     :param touch:
    #     :return:
    #     """
    #     play_btn_ding_sound()
    #     return super().on_touch_down(touch)

    pass
