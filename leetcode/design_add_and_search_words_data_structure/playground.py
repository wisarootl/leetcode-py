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
from helpers import assert_word_dictionary, run_word_dictionary
from solution import WordDictionary

# %%
# Example test case
operations = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
inputs = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
expected = [None, None, None, None, False, True, True, True]

# %%
result = run_word_dictionary(WordDictionary, operations, inputs)
result

# %%
assert_word_dictionary(result, expected)
