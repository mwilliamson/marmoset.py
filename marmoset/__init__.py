import sys


if sys.version_info[0] == 2:
    _literal_types = (int, long, float, basestring)
    _iteritems = lambda x: x.iteritems()
else:
    _literal_types = (int, float, str)
    _iteritems = lambda x: x.items()


def dump(value, output):
    output.write(dumps(value).encode("utf8"))


def dumps(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif isinstance(value, _literal_types):
        return str(value)
    elif isinstance(value, list):
        element_strs = map(_dumps_element, value)
        return _join_with_newline_spacing(element_strs)
    elif isinstance(value, dict):
        key_value_strs = [
            (dumps(item_key), dumps(item_value))
            for item_key, item_value in _iteritems(value)
        ]
        
        max_key_length = max(len(key) for key, value in key_value_strs)
        item_strs = [
            "{0:>{width}}: {1}".format(key, _indent(value, max_key_length + 2), width=max_key_length)
            for key, value in key_value_strs
        ]
        
        return _join_with_newline_spacing(item_strs)


def _dumps_element(element):
    output = _indent(dumps(element), 2)
    return "- {0}".format(output)


def _indent(value, indentation):
    return value.replace("\n", "\n" + " " * indentation)


def _join_with_newline_spacing(values):
    output = []
    
    previous = None
    for value in values:
        if previous is not None:
            output.append("\n")
            if "\n" in previous or "\n" in value:
                output.append("\n")
                
        output.append(value)
        
        previous = value
        
    return "".join(output)
