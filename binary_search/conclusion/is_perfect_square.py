class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True

        left = 2
        right = num // 2

        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid**2 < num:
                left = mid+1
            else:
                right = mid-1
        
        return False

num = 2
sol = Solution()
print(sol.isPerfectSquare(num))