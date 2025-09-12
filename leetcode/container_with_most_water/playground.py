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
from helpers import assert_max_area, run_max_area
from solution import Solution

# %%
# Example test case
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
expected = 49

# %%
result = run_max_area(Solution, height)
result

# %%
assert_max_area(result, expected)
