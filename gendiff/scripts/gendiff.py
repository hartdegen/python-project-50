import argparse


def main():
    parser = argparse.ArgumentParser(prog="gendiff", description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", default="check_string_for_empty")
    parser.add_argument("second_file", default="check_string_for_empty")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
