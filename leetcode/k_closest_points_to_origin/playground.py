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
from helpers import assert_k_closest, run_k_closest
from solution import Solution

# %%
# Example test case
points = [[1, 3], [-2, 2]]
k = 1
expected = [[-2, 2]]

# %%
result = run_k_closest(Solution, points, k)
result

# %%
assert_k_closest(result, expected)
