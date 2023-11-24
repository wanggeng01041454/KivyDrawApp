import os

# 设置 kivy 的窗口环境变量
os.environ['KIVY_TEXT'] = 'pil'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class MyPaintApp(App):

    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()



# 能够输出 PIL.Image.Image 类型的图片，并经网络，无损压缩编码后传输到服务端；同时从服务端接收
# todo
# 基于kivy的良好操作界面，进行画图基本操作；同时提供提示词输入的地方
# 将画图结果转换为 PIL.Image.Image 类型的数据；
# 将数据进行无损压缩， zip, 7z 等
# 经网路发送到服务端， 使用proto buf
# 从服务端接收压缩后的图片数据；并解压缩后展示；
# 从服务器接收的数据可以保存在本地

