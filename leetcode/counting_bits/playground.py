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
from helpers import assert_count_bits, run_count_bits
from solution import Solution

# %%
# Example test case
n = 2
expected = [0, 1, 1]

# %%
result = run_count_bits(Solution, n)
result

# %%
assert_count_bits(result, expected)
