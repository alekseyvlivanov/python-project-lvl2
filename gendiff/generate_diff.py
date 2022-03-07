# -*- coding: utf-8 -*-

from gendiff.parsers import parse_content
from gendiff.utils import get_file_content, get_file_type


def build_diff(first_data, second_data):
    def build_node(key):
        if key not in first_data:
            return {"key": key, "status": "added", "value": second_data[key]}

        if key not in second_data:
            return {"key": key, "status": "removed", "value": first_data[key]}

        first_value = first_data[key]
        second_value = second_data[key]

        if first_value == second_value:
            return {"key": key, "status": "unmodified", "value": second_value}

        if isinstance(first_value, dict) and isinstance(second_value, dict):
            return {
                "key": key,
                "status": "nested",
                "nested": build_diff(first_value, second_value),
            }

        return {"key": key, "status": "modified", "value": (first_value, second_value)}

    keys = sorted(set(first_data) | set(second_data))

    return list(map(build_node, keys))


def format_diff(diff_data):
    markers = {"added": "+ ", "removed": "- ", "unmodified": "  "}

    indent = "  "
    result = "{\n"

    for obj in diff_data:
        key = obj["key"]
        status = obj["status"]
        value = obj["value"]

        if type(value) == bool:
            value = str(value).lower()

        if status == "modified":
            result += "{}{}{}: {}\n".format(indent, markers["removed"], key, value[0])
            result += "{}{}{}: {}\n".format(indent, markers["added"], key, value[1])
        else:
            result += "{}{}{}: {}\n".format(indent, markers[status], key, value)

    return result + "}"


def generate_diff(first_file, second_file):
    first_file_content = get_file_content(first_file)
    second_file_content = get_file_content(second_file)

    first_file_type = get_file_type(first_file)
    second_file_type = get_file_type(second_file)

    first_file_data = parse_content(first_file_content, first_file_type)
    second_file_data = parse_content(second_file_content, second_file_type)

    diff_data = build_diff(first_file_data, second_file_data)
    formatted_data = format_diff(diff_data)

    return formatted_data
