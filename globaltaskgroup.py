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


class GlobalTaskGroup(metaclass=SingletonMeta):
    """
    全局的协程管理器
    因为 python 3.10 版本时尚且没有 asyncio 的 TaskGroup 类，
    所以自己实现一个简易版的 TaskGroup 类
    """

    _tasks = set()

    def create_task(self, coro, *, name=None):
        """简单封装 asyncio.create_task 方法"""
        t = asyncio.create_task(coro, name=name)
        self._tasks.add(t)
        t.add_done_callback(self._on_task_done)

    def _on_task_done(self, task):
        self._tasks.discard(task)

    def cancel_all(self):
        """取消所有的协程任务"""
        for t in self._tasks:
            if not t.done():
                t.cancel()
        pass
    pass

