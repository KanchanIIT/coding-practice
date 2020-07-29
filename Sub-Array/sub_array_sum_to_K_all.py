"""
SUBARRAY SUM FIND ALL RESULT

Problem:
    given array of integers (both positive and negatives) and K, find if the there is any subarray whole sum is K
Example:
    input:
        nums = [1,4,20,3,10,5]
        K = 33
    output:
        [2,4]   # values within index 2 and 4 --> [20,3,10] has sum equal to 33

     input:
        nums = [10, 2, -2, -20, 10]
        K = -10
    output:
        [0,3]   # values within index 0 and 3 --> [10, 2, -2, -20] has sum equal to -10

Find subarray sum to k
both (+ve) and (-ve) numbers
Find any solution if it has.

                cur_sum = 38
     cur_sum =5       |
        |             |
--------|-------------|-----
| 1 | 4 | 20 | 3 | 10 | 5 |
--------|-------------|-----
        |<----------->|
    index = 1         |
            cur_sum - target = 5
"""


def sub_array_sum(nums: list, K: int) -> list:
    res = list()
    d = dict()
    cur_sum = 0  # current sum so far
    for idx, i in enumerate(nums):
        cur_sum += nums[idx]
        if cur_sum == K:
            res.append([0, idx])
        elif (cur_sum - K) in d:
            res.append([d[cur_sum - K]+1, idx])   ## please be carefull, here we have to add +1
        else:
            d[cur_sum] = idx  ### be carefull here, need to push only
    return res  # nothing found


if __name__ == "__main__":
    nums = [1, 4, 20, 3, 10, 5, 33, 0]
    K = 33
    print(sub_array_sum(nums, K))
    # ans [[2, 4], [6, 6], [6, 7]]
