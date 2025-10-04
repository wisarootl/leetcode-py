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
from helpers import assert_add_two_numbers, run_add_two_numbers
from solution import Solution

# %%
# Example test case
l1_vals = [2, 4, 3]
l2_vals = [5, 6, 4]
expected_vals = [7, 0, 8]

# %%
result = run_add_two_numbers(Solution, l1_vals, l2_vals)
result

# %%
assert_add_two_numbers(result, expected_vals)
