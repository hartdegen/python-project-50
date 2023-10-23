from gendiff.parsers import MAPPING


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


def generate_diff(dict1, dict2, ext):
    before = MAPPING[ext](dict1)
    after = MAPPING[ext](dict2)
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