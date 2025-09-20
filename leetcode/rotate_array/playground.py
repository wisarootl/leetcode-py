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
from helpers import assert_rotate, run_rotate
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
expected = [5, 6, 7, 1, 2, 3, 4]

# %%
result = run_rotate(Solution, nums, k)
result

# %%
assert_rotate(result, expected)
