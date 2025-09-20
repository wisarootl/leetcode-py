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
from helpers import assert_find_order, run_find_order
from solution import Solution

# %%
# Example test case
num_courses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
expected = [0, 2, 1, 3]

# %%
result = run_find_order(Solution, num_courses, prerequisites)
result

# %%
assert_find_order(result, expected)
