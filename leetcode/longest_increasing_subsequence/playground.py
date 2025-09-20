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
from helpers import assert_length_of_lis, run_length_of_lis
from solution import Solution

# %%
# Example test case
nums = [10, 9, 2, 5, 3, 7, 101, 18]
expected = 4

# %%
result = run_length_of_lis(Solution, nums)
result

# %%
assert_length_of_lis(result, expected)
