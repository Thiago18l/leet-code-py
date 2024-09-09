from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    """
    if not strs:
        return ""
    min_len = min(len(s) for s in strs)
    for i in range(min_len):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[j - 1][i]:
                return strs[0][:i]
    return strs[0][:min_len]


test_cases = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
results = ["fl", ""]
for i, test_case in enumerate(test_cases):
    longest_common_prefix(test_case) == results[i]
    print(f"Test case {i + 1}: {longest_common_prefix(test_case)}")
