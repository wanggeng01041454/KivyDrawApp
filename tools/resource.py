# -*- coding: utf-8 -*-
"""
定义全局的资源文件管理器
"""
import yaml
from kivy.core.audio import SoundLoader

from .singletonmeta import SingletonMeta


class ResourceManager(metaclass=SingletonMeta):
    """
    资源管理器
    """
    """按钮声音"""
    _btn_ding_sound = None

    """语言文件"""
    _en_lang_dict = None
    _zh_lang_dict = None
    _default_lang_dict = None
    _zh_lang_font = 'res/font/msyh.ttc'
    _default_lang_font = ''

    def __init__(self):
        # 加载按钮的声音文件
        self._btn_ding_sound = SoundLoader.load("res/sound/button-ding.wav")
        self._load_language()

    def play_btn_sound(self):
        self._btn_ding_sound.play()
        pass

    def _load_language(self):
        """
        加载语言文件
        :return:
        """
        self._en_lang_dict = yaml.load(open("res/language/en.yaml", encoding="utf-8"), Loader=yaml.FullLoader)
        self._zh_lang_dict = yaml.load(open("res/language/zh.yaml", encoding="utf-8"), Loader=yaml.FullLoader)
        pass

    def set_language(self, lang: str):
        """
        设置语言
        :param lang:
        :return:
        """
        if lang == "en":
            self._default_lang_dict = self._en_lang_dict
            self._default_lang_font = ''
        elif lang == "zh":
            self._default_lang_dict = self._zh_lang_dict
            self._default_lang_font = self._zh_lang_font
        else:
            raise ValueError("unknown language type: {}".format(lang))
        pass

    def get_lang_text(self, *args, embed_font: bool = False) -> str:
        """
        按照 keys 获取语言文本
        embed_font 参数，是为了兼容 kivymd 中某些组建没有 font_name 的场景
        :param args: 语言文本的键值
        :param embed_font: 是否嵌入字体
        :return: 语言文本
        """
        cur_dict = self._default_lang_dict
        for key in args:
            cur_dict = cur_dict[key]

        # 只有字体不为空时，才需要真正潜入字体
        if embed_font & (self._default_lang_font != ''):
            return '[font={}]{}[/font]'.format(self._default_lang_font, cur_dict)
        else:
            return cur_dict
        pass

    def get_lang_font(self) -> str:
        """
        获取语言字体
        :return:
        """
        return self._default_lang_font

    pass
