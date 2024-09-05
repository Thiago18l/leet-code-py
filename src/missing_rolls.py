from typing import List


def missingRolls(rolls: List[int], mean: int, n: int) -> List[int]:
    """
    You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

    You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

    Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

    The average value of a set of k numbers is the sum of the numbers divided by k.

    Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

    """
    m = len(rolls)
    total = mean * (n + m)
    sum_existing = sum(rolls)
    total -= sum_existing
    if total < n or total > 6 * n:
        return []
    quotient, remainder = divmod(total, n)
    result = [quotient] * n
    for i in range(remainder):
        result[i] += 1
    return result


test_cases = [([3, 2], 4, 2), ([1, 5, 6], 3, 4), ([1, 2, 3, 4], 6, 4)]
results = [[6, 6], [2, 2, 2, 2], []]
print(missingRolls(*test_cases[1]), results[1])
