# -*- coding: utf-8 -*-

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

