#!/usr/bin/env python
# -*-coding:utf-8-*-

import json
from pkg_resources import resource_filename, resource_string


def test_json_data():
    f = open(resource_filename("my_fake_useragent", "data.json"),
             encoding='utf8')

    res = json.load(f)
    assert res is not None

