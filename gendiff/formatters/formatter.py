from gendiff.formatters.stylish import make_stylish_string


def make_dict(status, key, value, prev_value=None):
    dictionary = {
        "key": key,
        "status": status,
        "prev_value": prev_value,
        "value": value,
    }
    return dictionary


def func(before, after):
    keys = list({**before, **after}.keys())
    keys.sort()
    def f(key):
        if key not in before:
            print('ADDED', key, after[key])
            return make_dict("added", key, after[key])
        if key not in after:
            print('DELETED', key, before[key])
            return make_dict("deleted", key, before[key])
        if key in before and key in after:
            if isinstance(before[key], dict) and isinstance(after[key], dict):
                print('NESTED', key)
                return make_dict("nested", key, func(before[key], after[key]))
            elif before[key] == after[key]:
                print('SAME', key, before[key])
                return make_dict("same", key, before[key])
            elif before[key] != after[key]:
                print('CHANGED', key, after[key], before[key])
                return make_dict("changed", key, after[key], before[key])
            
    l = list(map(f, keys))
    return l

def generate_diff(before, after):
    l = func(before, after)
    result = make_stylish_string(l)
    return result
