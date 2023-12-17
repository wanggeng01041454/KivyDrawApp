# -*- coding: utf-8 -*-

from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField


class PromptDialog(MDDialog):
    """
    输入提示词对话框
    """
    """输入框"""
    text_field: MDTextField = None

    def __init__(self, **kwargs):
        """
        构造函数
        :param kwargs:
        """

        self._create_text_field()
        super().__init__(
            type="custom",
            title="please input prompt word",
            content_cls=self.text_field,
            **kwargs)
        pass

    def _create_text_field(self) -> None:
        """
        创建输入框
        """
        self.text_field = MDTextField(
            multiline=False,
            mode="rectangle",
            required=True,
        )
        pass

    def get_prompt_word(self) -> str:
        """
        获取输入的提示词
        :return:
        """
        return self.text_field.text
    pass
