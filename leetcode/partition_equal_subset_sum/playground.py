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
from helpers import assert_can_partition, run_can_partition
from solution import Solution

# %%
# Example test case
nums = [1, 5, 11, 5]
expected = True

# %%
result = run_can_partition(Solution, nums)
result

# %%
assert_can_partition(result, expected)
