def isBadVersion(version: int) -> bool:
    if version > 2315:
        return True
    else:
        return False
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
x = Solution()
print(x.firstBadVersion(64000))