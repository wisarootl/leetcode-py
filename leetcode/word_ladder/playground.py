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
from helpers import assert_ladder_length, run_ladder_length
from solution import Solution

# %%
# Example test case
begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
expected = 5

# %%
result = run_ladder_length(Solution, begin_word, end_word, word_list)
result

# %%
assert_ladder_length(result, expected)
