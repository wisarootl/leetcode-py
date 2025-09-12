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
from helpers import assert_spiral_order, run_spiral_order
from solution import Solution

# %%
# Example test case
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]

# %%
result = run_spiral_order(Solution, matrix)
result

# %%
assert_spiral_order(result, expected)
