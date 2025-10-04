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
from helpers import assert_find_min, run_find_min
from solution import Solution

# %%
# Example test case
nums: list[int] = [3, 4, 5, 1, 2]
expected: int = 1

# %%
result = run_find_min(Solution, nums)
result

# %%
assert_find_min(result, expected)
