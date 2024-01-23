def findPeakElement(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr)-1
        while lo < hi:
            mid = (lo + hi) // 2

            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            if arr[mid+1] > arr[mid]:
                lo = mid+1
            elif arr[mid-1] > arr[mid]:
                hi = mid

        return lo
