# -*- coding: utf-8 -*-
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.button import MDIconButton

# 默认的按钮图标大小
DEFAULT_BUTTON_ICON_SIZE = 64
# 被选中的按钮图标大小
SELECTED_BUTTON_ICON_SIZE = 96
# hover 时的按钮图标大小
HOVER_BUTTON_ICON_SIZE = 128


class MDIconHoverButton(MDIconButton, HoverBehavior):
    def __init__(self, **kwargs):
        """
        构造函数，初始化为默状态
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.set_normal_state()
        pass

    """
    带有 hover 效果的 MDIconButton
    """
    def set_hover_state(self):
        """
        设置鼠标滑过时的状态
        :return:
        """
        self.icon_size = HOVER_BUTTON_ICON_SIZE
        self.size_hint_x = 1
        self.size_hint_y = 2
        self.pos_hint = {"center_x": 0.5, "center_y": 1}
        self.md_bg_color = [1, 1, 1, 0]
        pass

    def set_normal_state(self):
        """
        设置正常状态
        :return:
        """
        self.icon_size = DEFAULT_BUTTON_ICON_SIZE
        self.size_hint_x = 1
        self.size_hint_y = 1
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.md_bg_color = [1, 1, 1, 0]
        pass

    def set_selected_state(self):
        """
        设置被选中状态
        :return:
        """
        self.icon_size = SELECTED_BUTTON_ICON_SIZE
        self.size_hint_x = 1
        self.size_hint_y = 1
        self.pos_hint = {"center_x": 0.5, "center_y": 1}
        self.md_bg_color = [0, 0.4, 0, 0.2]

    pass
