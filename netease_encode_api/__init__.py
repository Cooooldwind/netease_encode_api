"""
netease_encode_api/__init__.py
Version: 1.2.0
Author: CooooldWind_, DeepSeek-R1, DeepSeek-V3, 豆包
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

import json
import requests
from base64 import b64encode
from Crypto.Cipher import AES
from netease_encode_api.global_args import GlobalArgs


class EncodeSession(requests.Session):
    # 继承自 requests.Session
    """
    WeAPI解码类（继承自requests.Session）
    """

    def __init__(self):
        super().__init__()
        # 显式调用父类初始化
        self.__global = GlobalArgs()
        self.__encode_arg_g = "0CoJUm6Qyw8W8jud"
        self.__encode_arg_i = "vlgPRPyGhwA6F4Sq"
        self.__encode_sec_key = self.__global.ENCODE_SEC_KEY
        # 固定为常见电脑Chrome浏览器的headers
        self.__headers = {
            'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.last_response: dict = None

    def __to_hex(self, encode_data):
        """
        16进制解码
        """
        temp = 16 - len(encode_data) % 16
        return encode_data + chr(temp) * temp

    def __encode_params(self, encode_data: str = "", encode_key: str = ""):
        """
        解码的关键函数(1)
        """
        func_iv = "0102030405060708"
        encode_data = self.__to_hex(encode_data)
        base64_sec_key = AES.new(
            key=encode_key.encode("utf-8"),
            iv=func_iv.encode("utf-8"),
            mode=AES.MODE_CBC,
        ).encrypt(encode_data.encode("utf-8"))
        return str(b64encode(base64_sec_key), "utf-8")

    def __get_params(self, encode_data: str = ""):
        """
        解码的关键函数(2)
        """
        return self.__encode_params(
            self.__encode_params(encode_data, self.__encode_arg_g), self.__encode_arg_i
        )

    def encoded_post(self, url: str, encode_data: dict) -> dict:
        """
        发送加密的POST请求并获取响应。
        需要给出 `url` 和 `encode_data` 作为参数。
        """
        processed_data = {
            "params": self.__get_params(json.dumps(encode_data)).encode("UTF-8"),
            "encSecKey": self.__encode_sec_key,
        }
        # 使用继承自父类的 post 方法
        response = self.post(
            url=url,
            data=processed_data,
            headers=self.__headers,
            timeout=10
        ).json()
        response = dict(response)
        self.last_response = response
        return response
