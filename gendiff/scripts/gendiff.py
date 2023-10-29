import argparse
import pathlib
from gendiff.parsers.parsers import MAPPING
from gendiff.formatters.formatter import make_format
from gendiff.formatters.stylish import make_stylish_string
from gendiff.formatters.plain import make_plain_string


def generate_diff(file_path1, file_path2, format_name="stylish"):
    with (
        open(file_path1) as f1,
        open(file_path2) as f2,
    ):
        file_extension = pathlib.Path(file_path1).suffix
        before = MAPPING[file_extension](f1)
        after = MAPPING[file_extension](f2)
        some_list = make_format(before, after)
        if format_name == "stylish":
            return make_stylish_string(some_list)
        if format_name == "plain":
            return make_plain_string(some_list)
        if format_name == "json":
            json_merged = {**before, **after}
            return json_merged


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", default="check_string_for_empty")
    parser.add_argument("second_file", default="check_string_for_empty")
    parser.add_argument("-f", "--format", help="set format of output",
                        default="stylish")
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    format_name = args.format
    diff = generate_diff(file_path1, file_path2, format_name)
    print(diff)


if __name__ == "__main__":
    main()
