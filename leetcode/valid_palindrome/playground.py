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
from helpers import assert_is_palindrome, run_is_palindrome
from solution import Solution

# %%
# Example test case
s = "A man, a plan, a canal: Panama"
expected = True

# %%
result = run_is_palindrome(Solution, s)
result

# %%
assert_is_palindrome(result, expected)
