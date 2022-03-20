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


def plain_value(value):
    if isinstance(value, dict):
        return "[complex value]"

    if type(value) == bool:
        return str(value).lower()

    if type(value) == str:
        return f"'{value}'"

    if value is None:
        return "null"

    return str(value)


def plainish(obj, ancestry):
    key = obj[KEY]
    status = obj[STATUS]
    value = obj[CHILDREN] if status == CHILDREN else obj[VALUE]

    ancestry_key = f"{ancestry}.{key}" if ancestry else f"{key}"

    if status == ADDED:
        return f"Property '{ancestry_key}' was added with value: {plain_value(value)}"

    if status == REMOVED:
        return f"Property '{ancestry_key}' was removed"

    if status == CHILDREN:
        return build_output(value, ancestry_key)

    if status == UNMODIFIED:
        return ""

    if status == MODIFIED:
        output_1 = f"Property '{ancestry_key}' was updated."
        output_2 = f"From {plain_value(value[0])} to {plain_value(value[1])}"

        return f"{output_1} {output_2}"

    raise Exception(f'Unknown status: "{status}" for key: "{ancestry_key}"')


def build_output(data, ancestry=""):
    output = filter(str, map(lambda x: plainish(x, ancestry), data))
    return "\n".join(output)


def format_plain(diff_data):
    return build_output(diff_data)
