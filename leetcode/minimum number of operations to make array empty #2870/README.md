You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

* Choose two elements with equal values and delete them from the array.
* Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

 

Example 1:

Input: nums = [2,3,3,2,2,4,2,3,4]
Output: 4
Explanation: We can apply the following operations to make the array empty:
- Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
- Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
- Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
- Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
It can be shown that we cannot make the array empty in less than 4 operations.
Example 2:

Input: nums = [2,1,2,2,3,3]
Output: -1
Explanation: It is impossible to empty the array.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 106


## explanation

we count how many times numbers are present in the list 
```py
nums_count = defaultdict(int)

for n in nums:
    nums_count[n] += 1
...
```

then we iter over the `nums_count`
```py
for n, c in nums_count.items():
```

if c is 1 we know that the list can't be empty, because it means there is a number without
any duplicates, so both of the requirements cant' be fulfilled

* Choose two elements with equal values and delete them from the array.
* Choose three elements with equal values and delete them from the array.

so we return `-1`, then we count how many times the number 3 can enter `c`, lets say we have this list, 
```py
[1,1,1,5,1,1,1,5,1,1]
# 1 count is 8
# 5 count is 2
```

$$8 // 3 = 2$$

now we know we can do 2 operations of subtracting `3` from the number `8`, we need to check if the number cannot be divided
by `3`, like 5, 7, 8 etc..., it means that the reminder is most likely 2, `8-((8//3)*3) = 2`, 

but if we had the number 10 `10-((10//3)*3) = 1`, the reminder would be `1` but it means we need to do the operation a bit differently like so:
$$10-3-3-2-2$$
this is 4 operations, `10//3 = 3` so if the number has a reminder `10 % 3` it we just `operations_count += 1`
