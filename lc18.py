#4 sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Pruning: smallest possible sum is already too large
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            # Pruning: largest possible sum is still too small
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Pruning
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result