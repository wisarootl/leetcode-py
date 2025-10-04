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
from helpers import assert_get_sum, run_get_sum
from solution import Solution

# %%
# Example test case
a = 1
b = 2
expected = 3

# %%
result = run_get_sum(Solution, a, b)
result

# %%
assert_get_sum(result, expected)
