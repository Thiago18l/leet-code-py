def palindrome_number(n: int) -> bool:
    if n < 0:
        return False
    return str(n) == str(n)[::-1]


def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10


test_cases = [121, -121, 10, -101]
print([palindrome_number(tc) for tc in test_cases])
print([isPalindrome(tc) for tc in test_cases])
