class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
       num = []
       for i in nums:
        num.append(i**2)
       num.sort()
       return num


     
        