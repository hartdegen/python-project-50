import json
from gendiff import generate_diff


def test_json():
    with (
        open('tests/fixtures/result.txt') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
        assert diff == result.read()


def test_yaml():
    with (
        open('tests/fixtures/result.txt') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
        assert diff == result.read()


def test_plain():
    with (
        open('tests/fixtures/result_plain.txt') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', "plain")
        assert diff == result.read()


def test_json():
    with (
        open('tests/fixtures/result_json.json') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.json', "json")
        assert diff == json.load(result)