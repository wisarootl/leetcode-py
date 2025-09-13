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
from helpers import assert_letter_combinations, run_letter_combinations
from solution import Solution

# %%
# Example test case
digits = "23"
expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# %%
result = run_letter_combinations(Solution, digits)
result

# %%
assert_letter_combinations(result, expected)
