# https://leetcode.com/problems/maximum-subarray/

# Kadanes's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0
        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            maxSum = max(currentSum, maxSum)
        return maxSum