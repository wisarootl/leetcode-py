# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_right_side_view, run_right_side_view
from solution import Solution

from leetcode_py import TreeNode

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, None, 5, None, 4]
expected = [1, 3, 4]

# %%
root = TreeNode.from_list(root_list)
root

# %%
result = run_right_side_view(Solution, root_list)
result

# %%
assert_right_side_view(result, expected)
