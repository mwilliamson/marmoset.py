try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict
import io

from nose.tools import istest, assert_equal

from marmoset import dumps, dump


@istest
def string_is_dumped_as_string_without_quotations():
    assert_equal("hello", dumps("hello"))


@istest
def integer_is_dumped_as_string():
    assert_equal("1", dumps(1))


@istest
def long_is_dumped_as_string():
    assert_equal("1", dumps(long(1)))


@istest
def long_is_dumped_as_string():
    assert_equal("1.2", dumps(1.2))


@istest
def booleans_are_dumped_as_lowercase_string():
    assert_equal("false", dumps(False))
    assert_equal("true", dumps(True))


@istest
def lists_are_dumped_with_each_element_on_new_line_preceded_by_hyphen():
    assert_equal("- 3\n- 2\n- 1", dumps([3, 2, 1]))
    
    
@istest
def nested_lists_cause_extra_indentation():
    assert_equal("- - 3\n  - 2", dumps([[3, 2]]))
    
    
@istest
def items_in_lists_are_separated_by_blank_line_if_they_are_multiline():
    assert_equal("- - 3\n  - 2\n\n- - 1\n  - 0", dumps([[3, 2], [1, 0]]))


@istest
def dumping_dicts_separates_key_and_value_with_colon_and_items_with_newlines():
    assert_equal(
        "one: 1\ntwo: 2",
        dumps(OrderedDict([("one", 1), ("two", 2)]))
    )


@istest
def keys_in_dicts_are_right_aligned():
    assert_equal(
        "a-long-key: 1\n     short: 2",
        dumps(OrderedDict([("a-long-key", 1), ("short", 2)]))
    )


@istest
def values_within_dicts_are_indented_if_they_are_on_multiple_lines():
    assert_equal(
        "one: - 3\n     - 2\n     - 1",
        dumps({"one": [3, 2, 1]})
    )


@istest
def multiline_dict_value_is_separated_by_newline_from_next_value():
    assert_equal(
        "one: - 3\n     - 2\n\ntwo: false",
        dumps(OrderedDict([("one", [3, 2]), ("two", False)]))
    )


@istest
def multiline_dict_value_is_separated_by_newline_from_previous_value():
    assert_equal(
        "two: false\n\none: - 3\n     - 2",
        dumps(OrderedDict([("two", False), ("one", [3, 2])]))
    )


@istest
def dump_writes_to_file_like_object():
    buf = io.BytesIO()
    dump(True, buf)
    assert_equal(b"true", buf.getvalue())
    
    
