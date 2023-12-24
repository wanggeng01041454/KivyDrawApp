# -*- coding: utf-8 -*-
from kivy.clock import Clock
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.button import MDIconButton

# 默认的背景色
DEFAULT_BUTTON_BACKGROUND_COLOR = [1, 1, 1, 0]
# 被选中的按钮背景色
SELECTED_BUTTON_BACKGROUND_COLOR = [0, 0.1, 0.78, 0.7]
# hover 时的按钮背景色
HOVER_BUTTON_BACKGROUND_COLOR = [0, 0.1, 0.78, 0.2]


class MDIconHoverButton(MDIconButton, HoverBehavior):
    def __init__(self, **kwargs):
        """
        构造函数，初始化为默状态
        :param kwargs:
        """
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.set_normal_state(), 0)
        pass

    """
    带有 hover 效果的 MDIconButton
    """
    def set_hover_state(self):
        """
        设置鼠标滑过时的状态
        :return:
        """
        self.md_bg_color = HOVER_BUTTON_BACKGROUND_COLOR
        pass

    def set_normal_state(self):
        """
        设置正常状态
        :return:
        """
        self.md_bg_color = DEFAULT_BUTTON_BACKGROUND_COLOR
        pass

    def set_selected_state(self):
        """
        设置被选中状态
        :return:
        """
        self.md_bg_color = SELECTED_BUTTON_BACKGROUND_COLOR

    pass
