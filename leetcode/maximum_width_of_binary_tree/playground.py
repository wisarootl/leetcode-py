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
from helpers import assert_width_of_binary_tree, run_width_of_binary_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 3, 2, 5, 3, None, 9]
expected = 4

# %%
result = run_width_of_binary_tree(Solution, root_list)
result

# %%
assert_width_of_binary_tree(result, expected)
