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
from helpers import assert_find_min_height_trees, run_find_min_height_trees
from solution import Solution

# %%
# Example test case
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
expected = [1]

# %%
result = run_find_min_height_trees(Solution, n, edges)
result

# %%
assert_find_min_height_trees(result, expected)
