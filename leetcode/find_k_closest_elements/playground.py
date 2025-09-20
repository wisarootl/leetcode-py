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
from helpers import assert_find_closest_elements, run_find_closest_elements
from solution import Solution

# %%
# Example test case
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
expected = [1, 2, 3, 4]

# %%
result = run_find_closest_elements(Solution, arr, k, x)
result

# %%
assert_find_closest_elements(result, expected)
