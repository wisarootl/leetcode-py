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
from helpers import assert_least_interval, run_least_interval
from solution import Solution

# %%
# Example test case
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
expected = 8

# %%
result = run_least_interval(Solution, tasks, n)
result

# %%
assert_least_interval(result, expected)
