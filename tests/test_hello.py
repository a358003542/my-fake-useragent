#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_fake_useragent import print_version


def test_version():
    assert print_version() == '0.1.0'

# if __name__ == '__main__':
