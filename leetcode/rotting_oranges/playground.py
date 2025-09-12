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
from helpers import assert_oranges_rotting, run_oranges_rotting
from solution import Solution

# %%
# Example test case
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
expected = 4

# %%
result = run_oranges_rotting(Solution, grid)
result

# %%
assert_oranges_rotting(result, expected)
