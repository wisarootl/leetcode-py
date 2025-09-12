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
from helpers import assert_combination_sum, run_combination_sum
from solution import Solution

# %%
# Example test case
candidates = [2, 3, 6, 7]
target = 7
expected = [[2, 2, 3], [7]]

# %%
result = run_combination_sum(Solution, candidates, target)
result

# %%
assert_combination_sum(result, expected)
