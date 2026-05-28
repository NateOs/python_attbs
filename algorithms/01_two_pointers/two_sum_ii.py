# Here’s a clean practice problem you can drop into your repo:

# ## Problem: Two Sum II (Sorted Array)

# You are given a **1-indexed** array of integers `numbers` sorted in non-decreasing order and an integer `target`.

# Find two numbers such that they add up to `target` and return their indices as a list `[index1, index2]`, where `1 <= index1 < index2 <= len(numbers)`.

# You may assume:
# - There is exactly one valid answer.
# - You may not use the same element twice.
# - Your solution must use **O(1)** extra space.

# ### Example 1
# Input: `numbers = [2, 7, 11, 15]`, `target = 9`  
# Output: `[1, 2]`  
# Explanation: `2 + 7 = 9`

# ### Example 2
# Input: `numbers = [1, 2, 3, 4, 6]`, `target = 6`  
# Output: `[2, 4]`  
# Explanation: `2 + 4 = 6`

# ### Constraints
# - `2 <= len(numbers) <= 3 * 10^4`
# - `-1000 <= numbers[i] <= 1000`
# - `numbers` is sorted in non-decreasing order
# - `-1000 <= target <= 1000`
# - Exactly one solution exists

# ### Function Signature (Python)
# ```python
# def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
#     pass
# ```

def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1


            
