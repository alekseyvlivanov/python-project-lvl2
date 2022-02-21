# -*- coding: utf-8 -*-


def get_file_content(file_path):
    with open(file_path) as file_object:
        return file_object.read()
