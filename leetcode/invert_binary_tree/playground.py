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
from helpers import assert_invert_tree, run_invert_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 7, 1, 3, 6, 9]
expected_list: list[int | None] = [4, 7, 2, 9, 6, 3, 1]

# %%
result = run_invert_tree(Solution, root_list)
result

# %%
assert_invert_tree(result, expected_list)
