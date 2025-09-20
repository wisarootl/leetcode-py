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
from helpers import assert_find_max_length, run_find_max_length
from solution import Solution

# %%
# Example test case
nums = [0, 1]
expected = 2

# %%
result = run_find_max_length(Solution, nums)
result

# %%
assert_find_max_length(result, expected)
