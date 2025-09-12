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
from helpers import assert_largest_rectangle_area, run_largest_rectangle_area
from solution import Solution

# %%
# Example test case
heights = [2, 1, 5, 6, 2, 3]
expected = 10

# %%
result = run_largest_rectangle_area(Solution, heights)
result

# %%
assert_largest_rectangle_area(result, expected)
