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
from helpers import assert_hamming_weight, run_hamming_weight
from solution import Solution

# %%
# Example test case
n = 11
expected = 3

# %%
result = run_hamming_weight(Solution, n)
result

# %%
assert_hamming_weight(result, expected)
