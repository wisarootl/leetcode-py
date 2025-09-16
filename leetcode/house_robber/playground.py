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
from helpers import assert_rob, run_rob
from solution import Solution

# %%
# Example test case
nums = [2, 7, 9, 3, 1]
expected = 12

# %%
result = run_rob(Solution, nums)
result

# %%
assert_rob(result, expected)
