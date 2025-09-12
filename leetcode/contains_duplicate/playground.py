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
from helpers import assert_contains_duplicate, run_contains_duplicate
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 1]
expected = True

# %%
result = run_contains_duplicate(Solution, nums)
result

# %%
assert_contains_duplicate(result, expected)
