def make_correct(arg):
    if isinstance(arg, bool):
        return str(arg).lower()
    if arg is None:
        return 'null'
    return arg


def set_value(item, count, space):
    if not isinstance(item, dict):
        return item
    pairs = item.items()

    def check_value(arg):
        return arg if not isinstance(arg, dict) else set_value(arg, count + 1, space)  # noqa: E501
    return "{" + ''.join([f"\n{space * (count + 1)}    {key}: {check_value(val)}" for key, val in pairs]) + f'\n{space * (count + 1)}' + "}"  # noqa: E501


def prerender(lst, depth=0):
    result = []
    for item in lst:
        if not isinstance(item, dict):
            return str(item)
        status, key, value, prev_value = (
            item["status"],
            item["key"],
            make_correct(item["value"]),
            make_correct(item["prev_value"]),
        )
        space = '    '
        match status:
            case "added":
                result.append(f"{space * depth}  + {key}: {set_value(value, depth, space)}")  # noqa: E501
            case "deleted":
                result.append(f"{space * depth}  - {key}: {set_value(value, depth, space)}")  # noqa: E501
            case "same":
                result.append(f"{space * depth}    {key}: {set_value(value, depth, space)}")  # noqa: E501
            case "changed":
                result.append(f"{space * depth}  - {key}: {set_value(prev_value, depth, space)}")  # noqa: E501
                result.append(f"{space * depth}  + {key}: {set_value(value, depth, space)}")  # noqa: E501
            case "nested":
                result.append(f"{space * depth}    {key}: {prerender(value, depth + 1)}")  # noqa: E501
            case _:
                raise ValueError(f"Warning: Unknown render case: '{status}'!")
    return "{\n" + "\n".join(result) + f"\n{space * depth}" + "}"


def make_stylish_string(some_list):
    return prerender(some_list)
