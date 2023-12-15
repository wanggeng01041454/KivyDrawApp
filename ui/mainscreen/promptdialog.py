# -*- coding: utf-8 -*-
from kivymd.uix.button import MDFlatButton
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

        ok_btn = MDFlatButton(
            text="OK",
            theme_text_color="Custom"
        )
        self._create_text_field()
        super().__init__(
            type="custom",
            content_cls=self.text_field,
            buttons=[ok_btn],
            **kwargs)
        pass

    def _create_text_field(self) -> None:
        """
        创建输入框
        """
        self.text_field = MDTextField(
                hint_text="input prompt word",
                helper_text="input prompt word",
                helper_text_mode="on_focus",
                required=True
            )
        pass

    pass
