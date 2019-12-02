#!/usr/bin/env python
# -*-coding:utf-8-*-

import random

from .utils import load_parsed_json_data
from .filter import filter_family, filter_os_family, filter_phone, \
    filter_version_range
from .utils import build_stream_function


class UserAgent():
    parsed_json_data = load_parsed_json_data()

    def __init__(self,
                 family=None,
                 os_family=None,
                 phone=None,
                 version_range=None,
                 ):
        """

        :param mode: default mode
        :param family: 不设置则不管 指定浏览器类型
        :param os_family: 不设置则不管 指定操作系统
        :param phone: 指定是否是手机端 True 是 False 不是 不设置默认None则不管
        :param version_range: 不设置则不管 指定浏览器版本范围

        手机检测 根据设备family参数之外 操作系统检测到 android 或 ios 也认为是移动端

        """

        if isinstance(family, str):
            family = family.lower()
            self.family = [family]
        elif isinstance(family, (list, tuple)):
            self.family = [f.lower() for f in family]
        elif family is None:
            self.family = None
        else:
            raise ValueError('family')

        if isinstance(os_family, str):
            os_family = os_family.lower()
            self.os_family = [os_family]
        elif isinstance(os_family, (list, tuple)):
            self.os_family = [f.lower() for f in os_family]
        elif os_family is None:
            self.os_family = None
        else:
            raise ValueError('os_family')

        self.phone = phone
        if self.phone not in [None, True, False]:
            raise ValueError('phone')

        self.version_range = version_range

        self.filter_func = build_stream_function(filter_family,
                                                 filter_os_family, filter_phone,
                                                 filter_version_range)

    def random(self):
        user_agent_list = self.get_useragent_list()

        if user_agent_list:
            return random.choice(user_agent_list)
        else:
            raise Exception('empty result')

    def get_useragent_list(self):
        origin_data = []
        for key in self.parsed_json_data:
            origin_data += self.parsed_json_data[key]

        d = {
            'data': origin_data,
            'family': self.family,
            'version_range': self.version_range,
            'os_family': self.os_family,
            'phone': self.phone
        }

        d = self.filter_func(d)

        ua_string_list = [i['string'] for i in d['data']]
        return ua_string_list

    def test_possible_family(self):
        t1 = set()
        for k, v in self.parsed_json_data.items():
            for i in v:
                t1.add(i['user_agent']['family'])
        return t1

    def test_possible_os_family(self):
        t1 = set()
        for k, v in self.parsed_json_data.items():
            for i in v:
                t1.add(i['os']['family'])
        return t1

    def test_possible_device_family(self):
        t1 = set()
        for k, v in self.parsed_json_data.items():
            for i in v:
                t1.add(i['device']['family'])
        return t1


__softname__ = 'my_fake_useragent'
__version__ = '0.1.6'


def print_version():
    return __version__

# if __name__ == '__main__':
