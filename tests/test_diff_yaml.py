# -*- coding: utf-8 -*-

from gendiff.generate_diff import generate_diff
from gendiff.utils import get_file_content


def test_diff_yaml():
    first_file = "./tests/fixtures/file1.yaml"
    second_file = "./tests/fixtures/file2.yml"
    diff_file = "./tests/fixtures/diff_file1_file2.txt"

    actual = generate_diff(first_file, second_file)
    expected = get_file_content(diff_file).strip()

    assert actual == expected