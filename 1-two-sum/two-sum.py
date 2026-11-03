class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        n = len(nums)
        for i in range(0,n):
            remain = target - nums[i]
            if remain in freq:
                return i, freq[remain]
            else:
                freq[nums[i]] = i
