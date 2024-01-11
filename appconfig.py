# -*- coding: utf-8 -*-

"""
配置整个kivy应用的配置文件
该文件的 config_app 函数必须在 main.py 中导入，并在导入任何 kivy 模块之前调用

发现一个奇怪的问题：
在按钮类中加载了一个声音文件，在点击按钮时播放声音，在ubuntu上运行时，不同的按钮居然音效有些差异;
但放在这里全局加载时，就是统一的音效了
"""
from kivy.config import Config

from kivy.core.audio import SoundLoader

"""按钮声音"""
ButtonDingSound = SoundLoader.load("res/sound/button-ding.wav")


def config_app() -> None:
    Config.set('graphics', 'multisamples', 8)
    pass


if __name__ == '__main__':
    pass
