# -*- coding: utf8 -*-

"""
定义和服务端通信协议相关的结构体
"""
import json
from enum import Enum


class ErrorCode(Enum):
    """
    错误码
    """
    pass


class ErrorMsg:
    """
    错误消息
    """
    code: ErrorCode = None
    msg: str = None

    def __init__(self, code: ErrorCode, msg: str):
        self.code = code
        self.msg = msg
        pass

    pass


class UploadManualPicture:
    """
    上传人工绘制的图片
    """

    @staticmethod
    def build_req(session: str, prompt: str, base64_img: str) -> str:
        """
        构造请求
        @param session: session id
        @param prompt: 提示词
        @param base64_img: base64编码的图片数据
        """
        obj = {
            "session_id": session,
            "prompt": prompt,
            "picture": base64_img
        }

        return json.dumps(obj)
        pass


