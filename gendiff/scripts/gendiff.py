import argparse
import json


def make_dict(status, key, value, deleted_value=None):
    return {
        "status": status,
        "key": key,
        "value": value,
        "deleted_value": deleted_value,
    }


def make_text_result(mapped):
    result = []
    for item in mapped:
        status, key, value, deleted_value = (
            item["status"],
            item["key"],
            str(item["value"]).lower()
            if isinstance(item["value"], bool)
            else item["value"],
            str(item["value"]).lower()
            if isinstance(item["deleted_value"], bool)
            else item["value"],
        )
        if status == "deleted":
            result.append(f"  - {key}: {value}")
        if status == "added":
            result.append(f"  + {key}: {value}")
        if status == "same":
            result.append(f"    {key}: {value}")
        if status == "changed":
            result.append(f"  - {key}: {deleted_value}")
            result.append(f"  + {key}: {value}")
    return "{\n" + "\n".join(result) + "\n}"


def generate_diff(before, after):
    keys = list({**before, **after}.keys())
    keys.sort()

    def f(key):
        if key not in after:
            return make_dict("deleted", key, before[key])
        if key not in before:
            return make_dict("added", key, after[key])
        if before[key] == after[key]:
            return make_dict("same", key, before[key])
        if before[key] != after[key]:
            return make_dict("changed", key, after[key], before[key])

    return make_text_result(map(f, keys))


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
    with (
        open(file_path1) as f1,
        open(file_path2) as f2,
    ):
        dict1 = json.load(f1)
        dict2 = json.load(f2)
        result = generate_diff(dict1, dict2)
        print(result)


if __name__ == "__main__":
    main()
