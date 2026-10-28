
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []

        for num in set(nums):
            if nums.count(num) > n // 3:
                result.append(num)

        return result
