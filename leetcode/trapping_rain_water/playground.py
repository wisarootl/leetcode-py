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
from helpers import assert_trap, run_trap
from solution import Solution

# %%
# Example test case
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
expected = 6

# %%
result = run_trap(Solution, height)
result

# %%
assert_trap(result, expected)
