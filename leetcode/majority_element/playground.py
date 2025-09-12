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
from helpers import assert_majority_element, run_majority_element
from solution import Solution

# %%
# Example test case
nums = [3, 2, 3]
expected = 3

# %%
result = run_majority_element(Solution, nums)
result

# %%
assert_majority_element(result, expected)
