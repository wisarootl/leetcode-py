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
from helpers import assert_subsets, run_subsets
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3]
expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# %%
result = run_subsets(Solution, nums)
result

# %%
assert_subsets(result, expected)
