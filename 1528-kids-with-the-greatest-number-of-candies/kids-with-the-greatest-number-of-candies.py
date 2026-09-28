class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n= list()
        max_candies = max(candies)
        for i in candies:
            n.append(i + extraCandies   >= max_candies)
        return n
        