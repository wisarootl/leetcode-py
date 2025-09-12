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
from helpers import assert_flood_fill, run_flood_fill
from solution import Solution

# %%
# Example test case
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

# %%
result = run_flood_fill(Solution, image, sr, sc, color)
result

# %%
assert_flood_fill(result, expected)
