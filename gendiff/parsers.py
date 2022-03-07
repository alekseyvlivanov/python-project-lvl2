# -*- coding: utf-8 -*-

import json
import yaml

parsers = {
    ".json": json.loads,
    ".yaml": yaml.safe_load,
    ".yml": yaml.safe_load,
}


def parse_content(file_content, file_type):
    if file_type in parsers:
        return parsers[file_type](file_content)
