# ---
# jupyter:
#   jupytext:
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
from helpers import assert_is_balanced, run_is_balanced
from solution import Solution

from leetcode_py import TreeNode

# %%
# Example test case
root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
expected = True

# %%
result = run_is_balanced(Solution, root_list)
result

# %%
root = TreeNode.from_list(root_list)
root

# %%
assert_is_balanced(result, expected)
