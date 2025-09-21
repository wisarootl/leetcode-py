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
from helpers import assert_file_system, run_file_system
from solution import FileSystem

# %%
# Example test case
operations = ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
inputs = [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
expected = [None, [], None, None, ["a"], "hello"]

# %%
result, fs = run_file_system(FileSystem, operations, inputs)
print(result)
fs

# %%
assert_file_system(result, expected)
