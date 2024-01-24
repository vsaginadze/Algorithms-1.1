def searchLeft(nums, target, l, r):
    if nums[l] == target:
        return l
    
    while l + 1 < r:
        m = (l + r) // 2
        if nums[m-1] != -1:
            if nums[m] == target:
                r = m
                if nums[m-1] != target:
                    return m
            elif nums[m] < target:
                l = m
            else:
                r = m
    if nums[l] == target: return l
    if nums[r] == target: return r

    return -1
        
def searchRight(nums, target, l, r):
    if nums[r] == target:
        return l
    
    while l + 1 < r:
        m = (l + r) // 2
        if nums[m+1] != len(nums)-1:
            if nums[m] == target:
                l = m
                if nums[m+1] != target:
                    return m
            elif nums[m] < target:
                l = m
            elif nums[m] > target:
                r = m
    if nums[l] == target: return l
    if nums[r] == target: return r
    return -1

def searchRange(nums, target):
    if len(nums) == 0:
        return (-1, -1)
    # if len(nums) == 2:
    #     return (0, 1)
    
    strt_idx, end_idx = (-1, -1)
    left, right = 0, len(nums)-1
    
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            strt_idx = searchLeft(nums, target, left, mid)
            end_idx = searchRight(nums, target, mid, right)
            return (strt_idx, end_idx)
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    
    if nums[left] == target and nums[right] == target:
        return (left, right)
    if nums[left] == target: return (left, left)
    if nums[right] == target: return (right, right)
    return (-1, -1)

ans = searchRange([0, 1, 1, 2, 3, 3, 5], 2)
print(ans)