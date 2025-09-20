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
from helpers import assert_top_k_frequent, run_top_k_frequent
from solution import Solution

# %%
# Example test case
words: list[str] = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
expected: list[str] = ["i", "love"]

# %%
result = run_top_k_frequent(Solution, words, k)
result

# %%
assert_top_k_frequent(result, expected)
