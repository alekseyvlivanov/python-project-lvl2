# -*- coding: utf-8 -*-

from gendiff.constants import (
    ADDED,
    CHILDREN,
    KEY,
    MODIFIED,
    REMOVED,
    STATUS,
    UNMODIFIED,
    VALUE,
)


def build_diff(first_data, second_data):
    def build_node(key):
        if key not in first_data:
            return {KEY: key, STATUS: ADDED, VALUE: second_data[key]}

        if key not in second_data:
            return {KEY: key, STATUS: REMOVED, VALUE: first_data[key]}

        first_value = first_data[key]
        second_value = second_data[key]

        if isinstance(first_value, dict) and isinstance(second_value, dict):
            return {
                KEY: key,
                STATUS: CHILDREN,
                CHILDREN: build_diff(first_value, second_value),
            }

        if first_value == second_value:
            return {KEY: key, STATUS: UNMODIFIED, VALUE: second_value}

        return {KEY: key, STATUS: MODIFIED, VALUE: (first_value, second_value)}

    keys = sorted(set(first_data) | set(second_data))

    return list(map(build_node, keys))
