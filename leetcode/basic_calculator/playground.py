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
from helpers import assert_calculate, run_calculate
from solution import Solution

# %%
# Example test case
s = "(1+(4+5+2)-3)+(6+8)"
expected = 23

# %%
result = run_calculate(Solution, s)
result

# %%
assert_calculate(result, expected)
