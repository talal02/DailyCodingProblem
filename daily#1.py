"""
Easy

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def first_solution(arr: list, k: int) -> bool:
    for i in range(len(arr)):
      for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == k:
          return True
    return False

"""
Explanation of first_solution:
- This solution is a brute force solution. We are checking every possible pair of numbers in the list to see if they add up to k.
- We are iterating through the list and checking every possible pair of numbers.
- If we find a pair that adds up to k, we return True.
"""

def bonus_solution(arr: list, k: int) -> bool:
    seen = set()
    for num in arr:
      if k - num in seen:
        return True
      seen.add(num)
    return False

"""
Explanation of bonus_solution:
- We are using a set to store the numbers we have seen so far.
- We are iterating through the list and checking if the difference between k and the current number is in the set.
- If it is, we return True.
"""

print(first_solution([10, 15, 3, 7], 17)) # True
print(bonus_solution([10, 15, 3, 7], 17)) # True
print(first_solution([10, 15, 3, 7], 20)) # False
print(bonus_solution([10, 15, 3, 7], 20)) # False
