# -*- coding: utf-8 -*-

import os.path


def get_file_content(file_path):
    with open(file_path) as file_object:
        return file_object.read()


def get_file_type(file_path):
    return os.path.splitext(file_path)[1]
