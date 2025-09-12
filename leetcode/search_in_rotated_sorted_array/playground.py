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
from helpers import assert_search, run_search
from solution import Solution

# %%
# Example test case
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
expected = 4

# %%
result = run_search(Solution, nums, target)
result

# %%
assert_search(result, expected)
