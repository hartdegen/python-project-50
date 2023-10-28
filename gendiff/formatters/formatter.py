def make_dict(status, key, value, prev_value=None):
    dictionary = {
        "key": key,
        "status": status,
        "prev_value": prev_value,
        "value": value,
    }
    return dictionary


def make_format(before, after):  # noqa: C901
    keys = list({**before, **after}.keys())
    keys.sort()

    def f(key):
        if key not in before:
            return make_dict("added", key, after[key])
        if key not in after:
            return make_dict("deleted", key, before[key])
        if key in before and key in after:
            if isinstance(before[key], dict) and isinstance(after[key], dict):
                return make_dict("nested", key,
                                 make_format(before[key], after[key]))
            elif before[key] == after[key]:
                return make_dict("same", key, before[key])
            elif before[key] != after[key]:
                ('CHANGED', key, after[key], before[key])
                return make_dict("changed", key, after[key], before[key])
    l = list(map(f, keys))
    return l
