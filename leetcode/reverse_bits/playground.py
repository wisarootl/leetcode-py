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
from helpers import assert_reverse_bits, run_reverse_bits
from solution import Solution

# %%
# Example test case
n: int = 43261596
expected: int = 964176192

# %%
result = run_reverse_bits(Solution, n)
result

# %%
assert_reverse_bits(result, expected)
