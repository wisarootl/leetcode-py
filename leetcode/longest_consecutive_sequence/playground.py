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
from helpers import assert_longest_consecutive, run_longest_consecutive
from solution import Solution

# %%
# Example test case
nums = [100, 4, 200, 1, 3, 2]
expected = 4

# %%
result = run_longest_consecutive(Solution, nums)
result

# %%
assert_longest_consecutive(result, expected)
