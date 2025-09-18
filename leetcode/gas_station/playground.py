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
from helpers import assert_can_complete_circuit, run_can_complete_circuit
from solution import Solution

# %%
# Example test case
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
expected = 3

# %%
result = run_can_complete_circuit(Solution, gas, cost)
result

# %%
assert_can_complete_circuit(result, expected)
