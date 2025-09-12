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
from helpers import assert_climb_stairs, run_climb_stairs
from solution import Solution

# %%
# Example test case
n = 3
expected = 3

# %%
result = run_climb_stairs(Solution, n)
result

# %%
assert_climb_stairs(result, expected)
