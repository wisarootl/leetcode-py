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
from helpers import assert_find_duplicate, run_find_duplicate
from solution import Solution

# %%
# Example test case
nums: list[int] = [1, 3, 4, 2, 2]
expected = 2

# %%
result = run_find_duplicate(Solution, nums)
result

# %%
assert_find_duplicate(result, expected)
