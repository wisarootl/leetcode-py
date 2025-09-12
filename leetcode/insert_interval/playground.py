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
from helpers import assert_insert, run_insert
from solution import Solution

# %%
# Example test case
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
expected = [[1, 5], [6, 9]]

# %%
result = run_insert(Solution, intervals, new_interval)
result

# %%
assert_insert(result, expected)
