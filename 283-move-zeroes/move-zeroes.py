class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        i = 0
        if n == 1:
            return nums
        while i<n:
            if nums[i] == 0:
                break
            i += 1
        if i == n:
            return nums
        j = i+1
        while j<n:
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
            j +=1 
        return nums
       