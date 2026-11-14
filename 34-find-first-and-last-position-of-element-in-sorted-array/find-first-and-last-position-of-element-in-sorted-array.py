
class Solution:

    def lowbnd(self, nums, target):
        n = len(nums)
        lb = -1
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1

        return lb

    def highbnd(self, nums, target):
        n = len(nums)
        hb = -1
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1
            else:
                hb = mid
                low = mid + 1

        return hb

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = self.lowbnd(nums, target)
        last = self.highbnd(nums, target)

        if first == -1 or nums[first] != target:
            return [-1, -1]

        return [first, last]




def highbnd(nums, target):
    n = len(nums)
    hb = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            hb = mid
            high = mid - 1
        else:
            low = mid + 1
    return hb
