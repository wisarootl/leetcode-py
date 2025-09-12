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
from helpers import assert_job_scheduling, run_job_scheduling
from solution import Solution

# %%
# Example test case
start_time = [1, 2, 3, 3]
end_time = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
expected = 120

# %%
result = run_job_scheduling(Solution, start_time, end_time, profit)
result

# %%
assert_job_scheduling(result, expected)
