# -*- coding: utf-8 -*-
import io
import os

from kivy.core.image import Image as CoreImage
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from ui import ui_image_screen_path

with open(
    os.path.join(ui_image_screen_path, "image_screen.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class ImageScreen(MDScreen):
    """
    展示图片的屏幕
    """
    image_widget: ObjectProperty(None)

    def set_image(self, image_data: bytes, fmt: str = 'png'):
        """
        设置图片
        测试代码：
        ```
        image_screen = ImageScreen(name='image_screen')
        file_name = str.format("/tmp/{}.png", 1)
        with open(file_name, 'rb') as f:
            image_screen.set_image(f.read())
        ```
        :param image_data: 图片数据
        :param fmt: 图片格式
        """
        bytes_io = io.BytesIO(image_data)
        self.image_widget.texture = CoreImage(bytes_io, ext=fmt).texture
        pass

    pass


