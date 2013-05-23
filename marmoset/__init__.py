def dump(value, output):
    output.write(dumps(value))


def dumps(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif isinstance(value, (int, long, float, basestring)):
        return str(value)
    elif isinstance(value, list):
        return "\n".join(
            _dumps_element(element)
            for element in value
        )
    elif isinstance(value, dict):
        key_value_strs = [
            (dumps(item_key), dumps(item_value))
            for item_key, item_value in value.iteritems()
        ]
        
        max_key_length = max(len(key) for key, value in key_value_strs)
        item_strs = [
            "{0:>{width}}: {1}".format(key, _indent(value, max_key_length + 2), width=max_key_length)
            for key, value in key_value_strs
        ]
        
        output = []
        
        previous = None
        for item_str in item_strs:
            if previous is not None:
                output.append("\n")
                if "\n" in previous or "\n" in item_str:
                    output.append("\n")
            output.append(item_str)
            
            previous = item_str
            
        return "".join(output)


def _dumps_element(element):
    output = _indent(dumps(element))
    if _is_scalar(element):
        return "- {0}".format(output)
    else:
        return "- {0}\n".format(output)


def _is_scalar(value):
    return not isinstance(value, (list, dict))


def _indent(value, indentation=2):
    return value.replace("\n", "\n" + " " * indentation)

