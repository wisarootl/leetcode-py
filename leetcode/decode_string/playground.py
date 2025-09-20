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
from helpers import assert_decode_string, run_decode_string
from solution import Solution

# %%
# Example test case
s = "3[a]2[bc]"
expected = "aaabcbc"

# %%
result = run_decode_string(Solution, s)
result

# %%
assert_decode_string(result, expected)
