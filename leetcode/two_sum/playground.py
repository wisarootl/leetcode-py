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
from helpers import assert_two_sum, run_two_sum
from solution import Solution

# %%
# Example test case
nums = [2, 7, 11, 15]
target = 9
expected = [0, 1]

# %%
result = run_two_sum(Solution, nums, target)
result

# %%
assert_two_sum(result, expected)
