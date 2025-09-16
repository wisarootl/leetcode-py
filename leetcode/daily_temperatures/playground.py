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
from helpers import assert_daily_temperatures, run_daily_temperatures
from solution import Solution

# %%
# Example test case
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
expected = [1, 1, 4, 2, 1, 1, 0, 0]

# %%
result = run_daily_temperatures(Solution, temperatures)
result

# %%
assert_daily_temperatures(result, expected)
