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
from helpers import assert_diameter_of_binary_tree, run_diameter_of_binary_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 4, 5]
expected = 3

# %%
result = run_diameter_of_binary_tree(Solution, root_list)
result

# %%
assert_diameter_of_binary_tree(result, expected)
