# -*- coding: utf-8 -*-

import asyncio
from globaltaskgroup import GlobalTaskGroup

# 导入配置文件，并在导入任何 kivy 模块之前调用
import appconfig
appconfig.config_app()

from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager

from ui.mainscreen.mainscreen import MainScreen


class MainApplication(MDApp):
    """
    This is the main application class of the app.
    """

    screen_manager = None
    main_screen = None

    def build(self):
        """
        This method is automatically called when the app is initialized
        :return:
        """
        Builder.load_file("kvs/mainui.kv")

        self.screen_manager = ScreenManager()
        self.main_screen = MainScreen()
        self.screen_manager.add_widget(self.main_screen)
        return self.screen_manager

    async def async_run_wrapper(self, task_group: GlobalTaskGroup):
        """
        包装 async_run 方法，
        在UI协程结束后，直接结束所有在执行协程
        """
        await self.async_run(async_lib='asyncio')
        # 显示协程结束后，直接结束所有在执行协程
        task_group.abort()

    async def run_with_asyncio_tg(self, task_group: GlobalTaskGroup):
        """
        Run the application with asyncio
        使用一个TaskGroup来管理所有的任务，在运行中，允许增加新的临时协程任务
        """
        async with task_group:
            task_group.create_task(self.async_run_wrapper(task_group))


if __name__ == '__main__':
    tg = GlobalTaskGroup()
    asyncio.run(MainApplication().run_with_asyncio_tg(tg))


# 能够输出 PIL.Image.Image 类型的图片，并经网络，无损压缩编码后传输到服务端；同时从服务端接收
# todo
# 基于kivy的良好操作界面，进行画图基本操作；同时提供提示词输入的地方
# 将画图结果转换为 PIL.Image.Image 类型的数据；
# 将数据进行无损压缩， zip, 7z 等
# 经网路发送到服务端， 使用proto buf
# 从服务端接收压缩后的图片数据；并解压缩后展示；
# 从服务器接收的数据可以保存在本地
