# -*- coding: utf-8 -*-


from gendiff.formatters import plain, stylish

formatters = {
    "plain": plain.format_plain,
    "stylish": stylish.format_stylish,
}


def format_diff(diff_data, output_format):
    if output_format not in formatters:
        raise Exception(f'"{output_format}" format is not supported yet')

    return formatters[output_format](diff_data)
