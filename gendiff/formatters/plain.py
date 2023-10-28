def make_correct(arg):
    if isinstance(arg, bool):
        return str(arg).lower()
    if isinstance(arg, str):
        return f"'{arg}'"
    if arg is None:
        return 'null'
    return arg


def set_value(item):
    if isinstance(item, dict):
        return '[complex value]'
    return f'{item}' if isinstance(item, str) else item


def prerender(some_list, full_path=''):  # noqa: C901
    result = []
    for item in some_list:
        status, key, value, prev_value = (
            item["status"],
            item["key"],
            make_correct(item["value"]),
            make_correct(item["prev_value"]),
        )
        path_to_verifiable_key = f'{full_path}.{key}'[1:]
        if status == 'added':
            result.append(f"Property '{path_to_verifiable_key}' was added with value: {set_value(value)}")  # noqa: E501
        elif status == 'deleted':
            result.append(f"Property '{path_to_verifiable_key}' was removed")
        elif status == 'changed':
            result.append(f"Property '{path_to_verifiable_key}' was updated. From {set_value(prev_value)} to {set_value(value)}")  # noqa: E501
        elif status == 'same':
            pass
        elif status == 'nested':
            result.extend(prerender(value, f'{full_path}.{key}'))
        else:
            raise ValueError(f"Warning: Unknown render case: '{status}'!")
    return result


def make_plain_string(some_list):
    return '\n'.join(prerender(some_list))
