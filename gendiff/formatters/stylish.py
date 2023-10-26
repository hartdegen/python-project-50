def set_value(item, count, space):
    if not isinstance(item, dict):
        return item
    pairs = item.items()
    def check_value(arg):
        return arg if not isinstance(arg, dict) else set_value(arg, count + 1, space)
    return "{" + ''.join([f"\n{space * (count + 1)}    {key}: {check_value(val)}" for key, val in pairs]) + f'\n{space * (count + 1)}' + "}"



def prerender(lst, depth=0):
    result = []
    for item in lst:
        if not isinstance(item, dict):
            return str(item)
        status, key, value, prev_value = (
            item["status"],
            item["key"],
            str(item["value"]).lower()
            if isinstance(item["value"], bool)
            else item["value"],
            str(item["prev_value"]).lower()
            if isinstance(item["prev_value"], bool)
            else item["prev_value"],
        )
        space = '    '
        match status:
            case "added":
                result.append(f"{space * depth}  + {key}: {set_value(value, depth, space)}")
            case "deleted":
                result.append(f"{space * depth}  - {key}: {set_value(value, depth, space)}")
            case "same":
                result.append(f"{space * depth}    {key}: {set_value(value, depth, space)}")
            case "changed":
                result.append(f"{space * depth}  - {key}: {set_value(prev_value, depth, space)}")
                result.append(f"{space * depth}  + {key}: {set_value(value, depth, space)}")
            case "nested":
                result.append(f"{space * depth}    {key}: {prerender(value, depth + 1)}")
            case _:
                raise ValueError(f"Warning: Unknown render case: '{status}'!")
    return "{\n" + "\n".join(result) +  f"\n{space * depth}" + "}"

def make_stylish_string(l):
    print(prerender(l))
