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
from helpers import assert_word_break, run_word_break
from solution import Solution

# %%
# Example test case
s = "leetcode"
word_dict = ["leet", "code"]
expected = True

# %%
result = run_word_break(Solution, s, word_dict)
result

# %%
assert_word_break(result, expected)
