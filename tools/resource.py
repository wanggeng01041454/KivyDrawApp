# -*- coding: utf-8 -*-
"""
定义全局的资源文件管理器
"""
from kivy.core.audio import SoundLoader

from .singletonmeta import SingletonMeta


class ResourceManager(metaclass=SingletonMeta):
    def __init__(self):
        """按钮声音"""
        self._btn_ding_sound = SoundLoader.load("res/sound/button-ding.wav")

    def play_btn_sound(self):
        self._btn_ding_sound.play()
        pass

    pass

