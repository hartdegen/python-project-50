from gendiff.scripts.gendiff import generate_diff


def test_json():
    with (
        open('tests/fixtures/result.txt') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', '.json')
        assert diff == result.read()


def test_yaml():
    with (
        open('tests/fixtures/result.txt') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', '.yaml')
        assert diff == result.read()