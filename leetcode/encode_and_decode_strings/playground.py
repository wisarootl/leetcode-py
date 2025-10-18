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
from helpers import assert_encode_decode, run_encode_decode
from solution import Solution

# %%
# Example test case
strs = ["Hello", "World"]
expected = strs

# %%
result = run_encode_decode(Solution, strs)
result

# %%
assert_encode_decode(result, expected)
