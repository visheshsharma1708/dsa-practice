class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            def isBadVersion(mid):
                ...

            if isBadVersion(mid):
                
                right = mid
            else:

                left = mid + 1

        return left