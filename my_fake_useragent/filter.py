#!/usr/bin/env python
# -*-coding:utf-8-*-

from ua_parser import user_agent_parser
import logging
from .const import FAMILY_MAP, PHONE_DEVICE_FAMILY_LIST, OS_FAMILY_MAP

logger = logging.getLogger(__name__)


def filter_family(d):
    data = d['data']
    family = d.get('family')

    if family:
        extend_family = []
        for i in family:
            if i in FAMILY_MAP:
                extend_item = FAMILY_MAP[i]
            else:
                extend_item = [i]
            extend_family += extend_item

        new_data = []
        for item_data in data:
            target_family = item_data['user_agent']['family']

            if target_family in extend_family:
                new_data.append(item_data)

        d['data'] = new_data
    return d


def filter_os_family(d):
    data = d['data']
    os_family = d.get('os_family')

    if os_family:
        extend_family = []
        for i in os_family:
            if i in OS_FAMILY_MAP:
                extend_item = OS_FAMILY_MAP[i]
            else:
                extend_item = [i]
            extend_family += extend_item

        new_data = []
        for item_data in data:
            target_os_family = item_data['os']['family']

            if target_os_family in extend_family:
                new_data.append(item_data)

        d['data'] = new_data
    return d


def filter_phone(d):
    data = d['data']
    phone = d.get('phone')

    if phone is None:
        return d
    extend_family = []
    for i in ['android', 'ios']:
        if i in OS_FAMILY_MAP:
            extend_item = OS_FAMILY_MAP[i]
        else:
            extend_item = [i]
        extend_family += extend_item

    if phone:
        new_data = []
        for item_data in data:
            target_device_family = item_data['device']['family']
            target_os_family = item_data['os']['family']

            if target_device_family in PHONE_DEVICE_FAMILY_LIST:
                new_data.append(item_data)
            elif target_os_family in extend_family:
                new_data.append(item_data)

        d['data'] = new_data
        return d
    else:
        # phone is False only return computer webbrower
        new_data = []
        for item_data in data:
            target_device_family = item_data['device']['family']
            target_os_family = item_data['os']['family']

            extend_family = []
            for i in ['android', 'ios']:
                if i in OS_FAMILY_MAP:
                    extend_item = OS_FAMILY_MAP[i]
                else:
                    extend_item = [i]
                extend_family += extend_item

            if target_device_family in PHONE_DEVICE_FAMILY_LIST:
                pass
            elif target_os_family in extend_family:
                pass
            else:
                new_data.append(item_data)

        d['data'] = new_data
        return d


def filter_version_range(d):
    data = d['data']
    version_range = d.get('version_range')
    if version_range is not None:
        logger.warning('not implement yet')
    return d
