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
from helpers import assert_time_map_operations, run_time_map_operations
from solution import TimeMap

# %%
# Example test case
operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
inputs = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
expected = [None, None, "bar", "bar", None, "bar2", "bar2"]

# %%
result = run_time_map_operations(TimeMap, operations, inputs)
result

# %%
assert_time_map_operations(result, expected)
