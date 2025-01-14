"""
Hard

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

"""

def first_solution(arr: list) -> list:
  products = []
  for i in range(len(arr)):
    product = 1
    for j in range(len(arr)):
      product *= arr[j] if i != j else 1
    products.append(product)
  return products


"""
Explanation of first_solution:
- We are iterating through the list and calculating the product of all the numbers except the one at the current index.
"""

def bonus_solution(arr: list) -> list:
  total_product = 1
  for num in arr:
    total_product *= num
  products = [total_product // num for num in arr]
  return products


"""
Explanation of bonus_solution:
- We are calculating the total product of all the numbers in the list.
- We are then iterating through the list and dividing the total product by the current number to get the product of all the numbers except the one at the current index.
"""

print(first_solution([1, 2, 3, 4, 5])) # [120, 60, 40, 30, 24]
print(bonus_solution([1, 2, 3, 4, 5])) # [120, 60, 40, 30, 24]
