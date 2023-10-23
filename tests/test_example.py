from gendiff.scripts.gendiff import generate_diff


def test_json():
    with (
        open('tests/fixtures/file1.json') as f1,
        open('tests/fixtures/file2.json') as f2,
        open('tests/fixtures/result.txt') as result,
    ):
        diff = generate_diff(f1, f2, '.json')
        assert diff == result.read()

def test_yaml():
    with (
        open('tests/fixtures/file1.yaml') as f1,
        open('tests/fixtures/file2.yaml') as f2,
        open('tests/fixtures/result.txt') as result,
    ):
        diff = generate_diff(f1, f2, '.yaml')
        assert diff == result.read()