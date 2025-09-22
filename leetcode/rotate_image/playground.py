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
from helpers import assert_rotate, run_rotate
from solution import Solution

# %%
# Example test case
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# %%
result = run_rotate(Solution, matrix)
result

# %%
assert_rotate(result, expected)
