#!/usr/bin/env python
# -*-coding:utf-8-*-

import re
import json
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

ALL_DETAIL_URL = 'http://www.useragentstring.com/pages/useragentstring.php?name=All'

WEB_TIMEOUT = 30


def write_json(file, data):
    with open(file, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def update_json_data():
    res = requests.get(ALL_DETAIL_URL, timeout=WEB_TIMEOUT)

    soup = BeautifulSoup(res.text, 'html5lib')

    liste = soup.find(id='liste')

    data = defaultdict(list)

    h3_text = None
    for item in liste.find_all(recursive=False):

        if item.name == 'h3':
            h3_text = item.text

            data[h3_text] = []

        if item.find_all('a'):
            a_list = item.find_all('a')
            for a in a_list:
                s = a.text
                # adjust
                if re.match('^More ', s):
                    continue

                if h3_text in data:
                    data[h3_text].append(s)

    write_json('data.json', data)

    return 0


def update_parsed_json_data():
    """
    更新parsed_json_data
    :return:
    """
    from .utils import load_json_data
    json_data = load_json_data()
    from ua_parser import user_agent_parser
    from collections import defaultdict
    new_json_data = defaultdict(list)

    for key, value in json_data.items():
        if value:
            for us_string in value:
                ua_parsed = user_agent_parser.Parse(us_string)
                item_data = dict(ua_parsed)
                new_json_data[key].append(item_data)
        else:
            new_json_data[key] = []

    write_json('parsed_data.json', new_json_data)

    return 0
