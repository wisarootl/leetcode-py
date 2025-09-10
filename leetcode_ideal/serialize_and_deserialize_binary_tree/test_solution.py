import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_serialize_deserialize, create_tree, run_serialize_deserialize


class TestSerializeAndDeserializeBinaryTree:
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
            ([0]),
            ([-1]),
            ([1000]),
            ([-1000]),
            ([1, 2, None, 3, None, 4, None]),
            ([1, None, 2, None, 3, None, 4]),
            ([-5, -3, -8, -2, -1, -7, -9]),
            ([0, -1, 1, -2, None, None, 2]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
            ([1, None, 2, None, 3, None, 4, None, 5]),
            ([1, 2, None, 3, None, 4, None, 5]),
            ([5, 4, 7, 3, None, 2, None, -1, None, 9]),
            ([1, 1, 1, 1, 1, 1, 1]),
            ([2, 2, None, 2, None]),
            ([10, 5, 15, None, 6, 12, 20, None, None, None, 13, 18, 25]),
            ([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]),
        ],
    )
    @logged_test
    def test_serialize_deserialize(self, root_list: list[int | None]):
        from .solution import Codec

        result = run_serialize_deserialize(Codec, root_list)
        expected = create_tree(root_list)
        assert_serialize_deserialize(result, expected)
