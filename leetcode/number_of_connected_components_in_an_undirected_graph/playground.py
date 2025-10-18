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
from helpers import assert_count_components, run_count_components
from solution import Solution

# %%
# Example test case
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
expected = 2

# %%
result = run_count_components(Solution, n, edges)
result

# %%
assert_count_components(result, expected)
