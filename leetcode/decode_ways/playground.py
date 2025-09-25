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
from helpers import assert_num_decodings, run_num_decodings
from solution import Solution

# %%
# Example test case
s = "226"
expected = 3

# %%
result = run_num_decodings(Solution, s)
result

# %%
assert_num_decodings(result, expected)
