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
from helpers import assert_top_k_frequent, run_top_k_frequent
from solution import Solution

# %%
# Example test case
nums = [1, 1, 1, 2, 2, 3]
k = 2
expected = [1, 2]

# %%
result = run_top_k_frequent(Solution, nums, k)
result

# %%
assert_top_k_frequent(result, expected)
