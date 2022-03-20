# -*- coding: utf-8 -*-

from gendiff.constants import (
    ADDED,
    CHILDREN,
    INDENT,
    KEY,
    MODIFIED,
    REMOVED,
    STATUS,
    UNMODIFIED,
    VALUE,
    MARKERS,
)


def style_value(value, level):
    if type(value) == bool:
        return str(value).lower()

    if value is None:
        return "null"

    if not isinstance(value, dict):
        return str(value)

    start_indent = INDENT * (level + 3)
    close_indent = INDENT * (level + 1)

    current_output = []

    for k, v in value.items():
        current_output.append(f"{start_indent}{k}: {style_value(v, level+2)}")

    current_output = ["{"] + current_output + [f"{close_indent}}}"]

    return "\n".join(current_output)


def stylish(obj, level):
    start_indent = INDENT * level
    close_indent = start_indent + INDENT

    key = obj[KEY]
    status = obj[STATUS]
    value = obj[CHILDREN] if status == CHILDREN else obj[VALUE]

    if status == ADDED:
        return f"{start_indent}{MARKERS[status]}{key}: {style_value(value, level)}"

    if status == REMOVED:
        return f"{start_indent}{MARKERS[status]}{key}: {style_value(value, level)}"

    if status == CHILDREN:
        output = build_output(value, level + 2)
        return f"{start_indent}{INDENT}{key}: {{\n{output}\n{close_indent}}}"

    if status == UNMODIFIED:
        return f"{start_indent}{MARKERS[status]}{key}: {style_value(value, level)}"

    if status == MODIFIED:
        output_removed = (
            f"{start_indent}{MARKERS[REMOVED]}{key}: {style_value(value[0], level)}"
        )
        output_added = (
            f"{start_indent}{MARKERS[ADDED]}{key}: {style_value(value[1], level)}"
        )

        return f"{output_removed}\n{output_added}"

    raise Exception(f'Unknown status: "{status}" for key: "{key}"')


def build_output(data, level=1):
    return "\n".join(map(lambda x: stylish(x, level), data))


def format_stylish(diff_data):
    return f"{{\n{build_output(diff_data)}\n}}"
