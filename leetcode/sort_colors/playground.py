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
from helpers import assert_sort_colors, run_sort_colors
from solution import Solution

# %%
# Example test case
nums = [2, 0, 2, 1, 1, 0]
expected = [0, 0, 1, 1, 2, 2]

# %%
result = run_sort_colors(Solution, nums)
result

# %%
assert_sort_colors(result, expected)
