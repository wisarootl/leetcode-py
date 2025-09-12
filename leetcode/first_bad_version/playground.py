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
from helpers import assert_first_bad_version, run_first_bad_version
from solution import Solution

# %%
# Example test case
n = 5
bad = 4
expected = 4

# %%
result = run_first_bad_version(Solution, n, bad)
result

# %%
assert_first_bad_version(result, expected)
