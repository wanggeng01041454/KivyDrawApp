# -*- coding: utf8 -*-
import asyncio

from collections.abc import Callable
from typing import Union

from globaltaskgroup import GlobalTaskGroup
from .protocal import *

"""接收到AI生成图片的回调函数"""
AiPictureCallbackFunc = Callable[[str], None]


class ConnManager:
    """
    连接管理器
    所有的异步函数都对外隐藏，只提供同步函数
    """

    """session_id: 代表和服务器端连接的session id； 只有连接建立后，才会有这个值"""
    _session_id: str = None
    """全局的协程管理器"""
    global_aio_tg: GlobalTaskGroup = GlobalTaskGroup()
    """向服务器发起请求的协程任务"""
    _request_task: Union[None, asyncio.Task] = None

    def process_manual_picture(self, prompt: str, base64_img: str, ai_pic_cb: AiPictureCallbackFunc):
        """
        使用AI处理人工绘制的图片数据，在成功处理后，会触发 on_ai_picture_event 事件
        @param prompt: 提示词
        @param base64_img: base64编码的图片数据
        """
        # 如果有正在等待的AI处理图片，则不处理
        if self._request_task is not None and not self._request_task.done():
            # todo, debug 打印输出
            return
        self._request_task = self.global_aio_tg.create_task(self._inner_deal_manual_picture(prompt, base64_img, ai_pic_cb))
        pass

    async def _inner_deal_manual_picture(self, prompt: str, base64_img: str, ai_pic_cb: AiPictureCallbackFunc):
        """
        处理人工绘制的图片数据
        @param prompt: 提示词
        @param base64_img: base64编码的图片数据
        """
        # 如果未建立连接，则先建立连接
        if self._session_id is None:
            await self._connect_server()

        # 发送图片数据, todo: 错误处理
        serial_no = await self._send_picture(prompt, base64_img)
        # 轮询，查询AI处理后的图片数据
        while True:
            # 查询AI处理后的图片数据, todo: 错误处理
            ai_img = await self._query_ai_picture(serial_no)
            await asyncio.sleep(1)
            # 收到图片数据，调用回调函数
            ai_pic_cb(ai_img)
            break

        # 协程完成，清除任务
        self._request_task = None
        pass

    async def _connect_server(self):
        """
        连接到服务端
        """
        # todo 实现初始连接协议
        self._session_id = "1234567890"
        pass

    async def _send_picture(self, prompt: str, base64_img: str) -> Union[ErrorMsg, int]:
        """
        发送图片数据
        @param prompt: 提示词
        @param base64_img: base64编码的图片数据
        @return: 返回 图片序列号，用于后续查询
        """
        req = UploadManualPicture.build_req(self._session_id, prompt, base64_img)
        # todo 模拟发送数据，后续调整为真实发送
        await asyncio.sleep(5)

        # todo
        return 0

    async def _query_ai_picture(self, serial_no: int) -> Union[ErrorMsg, str]:
        """
        查询AI处理后的图片数据
        @param serial_no: 图片序列号
        @return: 返回 base64编码的图片数据
        """
        # todo 模拟发送数据，后续调整为真实发送
        await asyncio.sleep(3)
        # todo
        return "xxxxxx"
