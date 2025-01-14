# Daily Coding Challenge Repository

This repository is dedicated to solving one coding problem daily to enhance problem-solving skills, algorithms, and coding proficiency. Each solution is organized and documented for easy reference. Join the journey of continuous learning!

---

## Problems Table

| Day   | Problem Description                                                                                                 | Difficulty | Asked By | Link to Solution      |
|-------|---------------------------------------------------------------------------------------------------------------------|------------|----------|------------------------|
| Day 1 | Given a list of numbers and a number `k`, determine if any two numbers in the list add up to `k`.                   | Easy       | Google   | [Solution](daily_1.py) |
| Day 2 | Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.                   | Hard       | Uber   | [Solution](daily_2.py) |

---

## Day 1 Problem Description

**Difficulty:** Easy
**Asked By:** Google

### Problem Statement

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

#### Example

- Input: `[10, 15, 3, 7]`, `k = 17`
- Output: `True` (since `10 + 7 = 17`)

**Bonus:** Can you solve this in one pass?

### Solutions

1. **Brute Force Solution**: Iterates through all pairs of numbers in the list to check if any two sum to `k`.
2. **Optimized Solution**: Utilizes a set to achieve a more efficient solution in a single pass.

For detailed implementations, see the [solution file](daily_1.py).

---

## Day 2 Problem Description

**Difficulty:** Hard
**Asked By:** Uber

### Problem Statement (2)

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#### Example (2)

- Input: `[1, 2, 3, 4, 5]`
- Output: `[120, 60, 40, 30, 24]`

### Solutions (2)

1. **Brute Force Solution**: Utilizes two nested loops to calculate the product of all the numbers except the one at the current index.
2. **Optimized Solution**: Calculates the total product of all the numbers in the list and then divides the total product by the current number to get the product of all the numbers except the one at the current index. This solution has a time complexity of O(n) and a space complexity of O(n).

For detailed implementations, see the [solution file](daily_2.py).

---
