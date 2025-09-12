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
from helpers import assert_coin_change, run_coin_change
from solution import Solution

# %%
# Example test case
coins = [1, 2, 5]
amount = 11
expected = 3

# %%
result = run_coin_change(Solution, coins, amount)
result

# %%
assert_coin_change(result, expected)
