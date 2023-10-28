from gendiff.scripts.gendiff import generate_diff


def test_json():
    with (
        open('tests/fixtures/result.txt') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "stylish")
        assert diff == result.read()


def test_yaml():
    with (
        open('tests/fixtures/result.txt') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', "stylish")
        assert diff == result.read()


def test_plain():
    with (
        open('tests/fixtures/result_plain.txt') as result,
    ):
        diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', "plain")
        assert diff == result.read()