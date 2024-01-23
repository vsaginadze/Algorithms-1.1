def firstBadVersion(self, num: int) -> int:
    if num == 0:
        return -1

    left, right = 0, num
    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    # Post-processing:
    # End Condition: left == right
    if isBadVersion(left):
        return left

    return -1
