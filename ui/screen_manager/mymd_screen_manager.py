# -*- coding: utf-8 -*-

from kivy.clock import Clock
from kivymd.uix.screenmanager import MDScreenManager

from ui.image_screen import ImageScreen
from ui.main_screen import MainScreen
from ui.wait_screen import WaitScreen


class MyMDScreenManager(MDScreenManager):
    """
    自定义的屏幕管理器
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 必须要有name属性，否则无法切换
        self._main_screen = MainScreen(name='main_screen')
        self._image_screen = None
        self._wait_screen = None

        self.add_widget(self._main_screen)

        # 绑定事件
        # 发送图片请求事件
        self._main_screen.bind(on_send_picture_request_event=self._on_send_picture_request_event_receiver)
        # 接收图片响应事件
        self._main_screen.bind(on_recv_picture_response_event=self._on_recv_picture_response_event_receiver)

        # 两个不会立即使用的屏幕，懒加载
        Clock.schedule_once(lambda dt: self._lazy_init(), 1)
        pass

    def _lazy_init(self):
        """
        懒加载
        """
        self._image_screen = ImageScreen(name='image_screen')
        self._wait_screen = WaitScreen(name='wait_screen')

        self.add_widget(self._image_screen)
        self.add_widget(self._wait_screen)
        pass

    def _on_send_picture_request_event_receiver(self, *args):
        """
        收到发送图片请求事件
        """
        self.switch_to(self._wait_screen)
        pass

    def _on_recv_picture_response_event_receiver(self, instance: any, image_data: bytes, fmt: str):
        """
        收到接收图片响应事件
        """
        self._image_screen.set_image(image_data, fmt)
        self.switch_to(self._image_screen)
        pass

    pass


