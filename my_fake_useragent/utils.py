#!/usr/bin/env python
# -*-coding:utf-8-*-

import json
from pkg_resources import resource_filename, resource_string
from functools import reduce
from .const import SUPPORT_TYPES


def load_json_data():
    f = open(resource_filename("my_fake_useragent", "data.json"),
             encoding='utf8')

    res = json.load(f)
    return res


def load_parsed_json_data():
    f = open(resource_filename("my_fake_useragent", "parsed_data.json"),
             encoding='utf8')

    res = json.load(f)

    new_res = {}
    for k in res:
        if k in SUPPORT_TYPES:
            new_res[k] = res[k]

    return new_res


def build_stream_function(*funcs):
    """
    构建流处理函数 函数参数更严格 只接受一个参数 d 字典值
    函数执行的顺序是从左到右
    :param funcs:
    :return:
    """

    return reduce(lambda f, g: lambda d: g(f(d)), funcs)
