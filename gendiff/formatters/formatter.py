import pathlib
from gendiff.parsers import MAPPING
from gendiff.formatters.stylish import make_stylish_string
from gendiff.formatters.plain import make_plain_string


def make_dict(status, key, value, prev_value=None):
    dictionary = {
        "key": key,
        "status": status,
        "prev_value": prev_value,
        "value": value,
    }
    return dictionary


def func(before, after):  # noqa: C901
    keys = list({**before, **after}.keys())
    keys.sort()

    def f(key):
        if key not in before:
            return make_dict("added", key, after[key])
        if key not in after:
            return make_dict("deleted", key, before[key])
        if key in before and key in after:
            if isinstance(before[key], dict) and isinstance(after[key], dict):
                return make_dict("nested", key, func(before[key], after[key]))
            elif before[key] == after[key]:
                return make_dict("same", key, before[key])
            elif before[key] != after[key]:
                ('CHANGED', key, after[key], before[key])
                return make_dict("changed", key, after[key], before[key])
    l = list(map(f, keys))
    return l


def generate_diff(file_path1, file_path2, format_name):
    with (
        open(file_path1) as f1,
        open(file_path2) as f2,
    ):
        file_extension = pathlib.Path(file_path1).suffix
        before = MAPPING[file_extension](f1)
        after = MAPPING[file_extension](f2)
        some_list = func(before, after)
        if format_name == "stylish":
            return make_stylish_string(some_list)
        if format_name == "plain":
            return make_plain_string(some_list)
        if format_name == "json":
            json_merged = {**before, **after}
            return json_merged
