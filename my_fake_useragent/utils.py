#!/usr/bin/env python
# -*-coding:utf-8-*-

from functools import reduce


def build_stream_function(*funcs):
    """
    构建流处理函数 函数参数更严格 只接受一个参数 d 字典值
    函数执行的顺序是从左到右
    :param funcs:
    :return:
    """

    return reduce(lambda f, g: lambda d: g(f(d)), funcs)
