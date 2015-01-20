from batteries.utils import Enum
from nose.tools import assert_equals


def test_enum_choices() :
    class TestEnum(Enum):
        A, B, C = 1, 2, 3

    test_enum = TestEnum()
    assert_equals(list(test_enum.choices()), [('A', 1), ('B', 2), ('C', 3)])
