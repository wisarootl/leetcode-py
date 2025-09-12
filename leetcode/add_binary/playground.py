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
from helpers import assert_add_binary, run_add_binary
from solution import Solution

# %%
# Example test case
a = "11"
b = "1"
expected = "100"

# %%
result = run_add_binary(Solution, a, b)
result

# %%
assert_add_binary(result, expected)
