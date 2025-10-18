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
from helpers import assert_valid_tree, run_valid_tree
from solution import Solution

# %%
# Example test case
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
expected = True

# %%
result = run_valid_tree(Solution, n, edges)
result

# %%
assert_valid_tree(result, expected)
