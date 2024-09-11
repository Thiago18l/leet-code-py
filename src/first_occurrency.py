class Solution:
    def str_index(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
