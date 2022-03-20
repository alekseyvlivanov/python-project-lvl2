# -*- coding: utf-8 -*-

from gendiff.build_diff import build_diff
from gendiff.formatters import format_diff
from gendiff.parsers import parse_content
from gendiff.utils import get_file_content, get_file_type


def generate_diff(first_file, second_file, output_format="stylish"):
    first_file_content = get_file_content(first_file)
    second_file_content = get_file_content(second_file)

    first_file_type = get_file_type(first_file)
    second_file_type = get_file_type(second_file)

    first_file_data = parse_content(first_file_content, first_file_type)
    second_file_data = parse_content(second_file_content, second_file_type)

    diff_data = build_diff(first_file_data, second_file_data)
    formatted_data = format_diff(diff_data, output_format)

    return formatted_data
