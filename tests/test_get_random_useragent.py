#!/usr/bin/env python
# -*-coding:utf-8-*-


from my_fake_useragent import UserAgent


def test():
    ua = UserAgent(family='chrome', os_family='linux')

    for i in range(100):
        res = ua.random()

        assert isinstance(res, str)
        assert len(res) > 0
        assert 'chrome' in res.lower()
