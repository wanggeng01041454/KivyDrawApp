# -*- coding: utf8 -*-

from .protocal import *


class ConnManager:
    """
    连接管理器
    """
    """session_id: 代表和服务器端连接的session id"""
    session_id: str = None

    def __init__(self):
        pass

    def connect(self):
        """
        连接到服务端
        """
        # todo 实现初始连接协议
        self.session_id = "1234567890"
        pass

    def disconnect(self):
        """
        断开与服务端的连接
        """
        pass

    def send_manual_picture(self, prompt: str, base64_img: str):
        """
        发送人工绘制的图片数据
        @param prompt: 提示词
        @param base64_img: base64编码的图片数据
        """
        req = UploadManualPicture.build_req(self.session_id, prompt, base64_img)
        # 测试代码，将其保存在文件中
        pass

    def is_connected(self) -> bool:
        """
        判断是否连接到了服务端
        """
        pass
