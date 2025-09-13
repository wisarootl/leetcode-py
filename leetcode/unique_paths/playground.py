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
from helpers import assert_unique_paths, run_unique_paths
from solution import Solution

# %%
# Example test case
m = 3
n = 7
expected = 28

# %%
result = run_unique_paths(Solution, m, n)
result

# %%
assert_unique_paths(result, expected)
