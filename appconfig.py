# -*- coding: utf-8 -*-

"""
    配置整个kivy应用的配置文件
    该文件的 config_app 函数必须在 main.py 中导入，并在导入任何 kivy 模块之前调用
"""
import asyncio
from kivy.config import Config


GlobalTaskGroup: asyncio.TaskGroup = asyncio.TaskGroup()



def config_app() -> None:
    Config.set('graphics', 'multisamples', 8)
    pass


if __name__ == '__main__':
    pass
