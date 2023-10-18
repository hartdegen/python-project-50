import json
from gendiff.scripts.gendiff import generate_diff


def test():
    with (
        open('tests/fixtures/file1.json') as f1,
        open('tests/fixtures/file2.json') as f2,
        open('tests/fixtures/result.txt') as result,
    ):
        dict1 = json.load(f1)
        dict2 = json.load(f2)
        diff = generate_diff(dict1, dict2)
        assert diff == result.read()