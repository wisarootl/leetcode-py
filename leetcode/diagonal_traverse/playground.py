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
from helpers import assert_find_diagonal_order, run_find_diagonal_order
from solution import Solution

# %%
# Example test case
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]

# %%
result = run_find_diagonal_order(Solution, mat)
result

# %%
assert_find_diagonal_order(result, expected)
