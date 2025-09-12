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
from helpers import assert_level_order, run_level_order
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
expected = [[3], [9, 20], [15, 7]]

# %%
result = run_level_order(Solution, root_list)
result

# %%
assert_level_order(result, expected)
