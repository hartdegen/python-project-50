import argparse
from gendiff.formatters.formatter import generate_diff


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
