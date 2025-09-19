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
from helpers import assert_group_anagrams, run_group_anagrams
from solution import Solution

# %%
# Example test case
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# %%
result = run_group_anagrams(Solution, strs)
result

# %%
assert_group_anagrams(result, expected)
