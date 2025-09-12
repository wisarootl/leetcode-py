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
from helpers import assert_three_sum, run_three_sum
from solution import Solution

# %%
# Example test case
nums = [-1, 0, 1, 2, -1, -4]
expected = [[-1, -1, 2], [-1, 0, 1]]

# %%
result = run_three_sum(Solution, nums)
result

# %%
assert_three_sum(result, expected)
