def searchLeft(nums, target, l, r):
    if nums[l] == target:
        return l
    
    while l + 1 < r:
        m = (l + r) // 2
        if nums[m-1]:
            if nums[m] == target and nums[m-1] != target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
    print(l, r)
    return -1
        
def searchRight(nums, target, l, r):
    if nums[l] == target:
        return l
    
    while l + 1 < r:
        m = (l + r) // 2
        if nums[m+1] != len(nums)-1:
            if nums[m] == target and nums[m+1] != target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
    print(l, r)
    return -1

def searchRange(nums, target):
    if len(nums) == 0:
        return (-1, -1)
    
    strt_idx, end_idx = (-1, -1)
    left, right = 0, len(nums)-1
    
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            strt_idx = searchLeft(nums, target, left, mid)
            end_idx = searchRight(nums, target, mid, right)
            print(strt_idx, end_idx)
            break
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    
    print("left", left)
    print("right", right)

searchRange([3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7], 5)