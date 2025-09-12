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
from helpers import assert_lru_cache, run_lru_cache
from solution import LRUCache

# %%
# Example test case
operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
expected = [None, None, None, 1, None, -1, None, -1, 3, 4]

# %%
result, cache = run_lru_cache(LRUCache, operations, inputs)
print(result)
cache.cache

# %%
assert_lru_cache(result, expected)
