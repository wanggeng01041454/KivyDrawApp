# -*- coding: utf-8 -*-
"""
定义全局的协程管理器
"""

import asyncio


class SingletonMeta(type):
    """
    单例元类
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        单例元类的 __call__ 方法
        :param args:
        :param kwargs:
        :return:
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            pass
        return cls._instances[cls]

    pass


class GlobalTaskGroup(asyncio.TaskGroup, metaclass=SingletonMeta):
    """
    全局的协程管理器
    """
    def abort(self):
        super()._abort()
        pass
    pass

