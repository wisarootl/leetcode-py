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
from helpers import assert_max_sub_array, run_max_sub_array
from solution import Solution

# %%
# Example test case
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected = 6

# %%
result = run_max_sub_array(Solution, nums)
result

# %%
assert_max_sub_array(result, expected)
