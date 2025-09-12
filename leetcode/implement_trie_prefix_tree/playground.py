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
from helpers import assert_trie_operations, run_trie_operations
from solution import Trie

# %%
# Example test case
operations = ["Trie", "insert", "search", "search", "starts_with", "insert", "search"]
inputs = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
expected = [None, None, True, False, True, None, True]

# %%
result, trie = run_trie_operations(Trie, operations, inputs)
print(result)
trie

# %%
assert_trie_operations(result, expected)
