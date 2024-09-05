def isMatch(s: str, p: str) -> bool:
    import re

    return re.fullmatch(p, s) is not None


def isMatch_v1(s: str, p: str) -> bool:
    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], "."}

    if len(p) >= 2 and p[1] == "*":
        return isMatch_v1(s, p[2:]) or first_match and isMatch_v1(s[1:], p)
    else:
        return first_match and isMatch_v1(s[1:], p[1:])


test_cases = [
    ("aa", "a"),
    ("aa", "a*"),
    ("ab", ".*"),
    ("aab", "c*a*b"),
    ("mississippi", "mis*is*p*."),
]
print([isMatch_v1(s, p) for s, p in test_cases])
