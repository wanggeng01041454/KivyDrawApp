# -*- coding: utf-8 -*-
import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from ui import ui_wait_screen_path

with open(
    os.path.join(ui_wait_screen_path, "wait_screen.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


# todo: 等待屏幕上的等待动画可以随机切换
class WaitScreen(MDScreen):
    """
    等待屏幕
    """
    pass
