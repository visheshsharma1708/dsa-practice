
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        distinct_nums = sorted(set(nums), reverse=True)

        if len(distinct_nums) >= 3:
            return distinct_nums[2]

        return distinct_nums[0]
