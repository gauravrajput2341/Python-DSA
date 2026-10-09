class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        temp = []
        for i in range(0,n):
            if nums[i] != 0:
                temp.append(nums[i])
                
        l = len(temp)
        for i in range(0,l):
            nums[i]= temp[i]
        for i in range(l,n):
            nums[i] = 0      