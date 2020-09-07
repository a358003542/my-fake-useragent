#!/usr/bin/env python
# -*-coding:utf-8-*-

import pytest
from my_fake_useragent.crawler import update_json_data, update_parsed_json_data


@pytest.mark.skip(reason="i have updated it")
def test_update_json_data():
    res = update_json_data()

    assert res == 0


@pytest.mark.skip(reason="i have updated it")
def test_update_parsed_json_data():
    res = update_parsed_json_data()

    assert res == 0
