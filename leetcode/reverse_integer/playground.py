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
from helpers import assert_reverse, run_reverse
from solution import Solution

# %%
# Example test case
x = 123
expected = 321

# %%
result = run_reverse(Solution, x)
result

# %%
assert_reverse(result, expected)
