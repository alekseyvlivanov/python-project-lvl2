# -*- coding: utf-8 -*-

from gendiff import generate_diff
from gendiff.utils import get_file_content


def test_diff_json_plain():
    first_file = "./tests/fixtures/file1.json"
    second_file = "./tests/fixtures/file2.json"
    diff_file = "./tests/fixtures/diff_file1_file2.plain"

    actual = generate_diff(first_file, second_file, output_format="plain")
    expected = get_file_content(diff_file).strip()

    assert actual == expected


def test_diff_json_stylish():
    first_file = "./tests/fixtures/file1.json"
    second_file = "./tests/fixtures/file2.json"
    diff_file = "./tests/fixtures/diff_file1_file2.stylish"

    actual = generate_diff(first_file, second_file, output_format="stylish")
    expected = get_file_content(diff_file).strip()

    assert actual == expected
