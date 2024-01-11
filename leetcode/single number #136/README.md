Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

## explanation
because the elements appear twice, we use xor because they will turn on their bits and turn them off,
for example 

```py
x = 5   # 0x101
x ^= 3  # will flip 0x11
x ^= 4  # will flip 0x100
x ^= 3  # will flip 0x11 back
x ^= 5  # will flip 0x101
# x = 4
```
