
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        # Step 1: Place each number at its correct index
        i = 0

        while i < n:

            correct_index = nums[i] - 1

            if (1 <= nums[i] <= n and
                nums[i] != nums[correct_index]):

                nums[i], nums[correct_index] = (
                    nums[correct_index], nums[i]
                )

            else:
                i += 1

        # Step 2: Find the first incorrect position
        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        # Step 3: All numbers from 1 to n are present
        return n + 1
