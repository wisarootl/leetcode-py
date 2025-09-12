import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_serialize_deserialize, run_serialize_deserialize
from .solution import Codec


class TestSerializeAndDeserializeBinaryTree:

    @logged_test
    @pytest.mark.parametrize(
        "root_list",
        [
            ([1, 2, 3, None, None, 4, 5]),
            ([]),
            ([1]),
            ([1, 2]),
            ([1, None, 2]),
            ([1, 2, 3, 4, 5, 6, 7]),
            ([5, 2, 3, None, None, 2, 4, 3, 1]),
        ],
    )
    def test_serialize_deserialize(self, root_list: list[int | None]):
        result = run_serialize_deserialize(Codec, root_list)
        assert_serialize_deserialize(result, root_list)
