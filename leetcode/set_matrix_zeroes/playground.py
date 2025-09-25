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
from helpers import assert_set_zeroes, run_set_zeroes
from solution import Solution

# %%
# Example test case
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

# %%
result = run_set_zeroes(Solution, matrix)
result

# %%
assert_set_zeroes(result, expected)
