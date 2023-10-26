import argparse
import pathlib
from gendiff.parsers import MAPPING
from gendiff.formatters.formatter import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", default="check_string_for_empty")
    parser.add_argument("second_file", default="check_string_for_empty")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    file_extension = pathlib.Path(file_path1).suffix
    with (
        open(file_path1) as f1,
        open(file_path2) as f2,
    ):
        before = MAPPING[file_extension](f1)
        after = MAPPING[file_extension](f2)
        result = generate_diff(before, after)
        print(result)


if __name__ == "__main__":
    main()
