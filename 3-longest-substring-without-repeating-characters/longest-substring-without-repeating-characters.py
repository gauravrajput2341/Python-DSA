class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = set()
        l1=0
        p = 0
        for i in range(len(s)):
            while s[i] in k:
                k.remove(s[l1])
                l1 += 1
            k.add(s[i]) 
            p= max(p,i-l1+1)
        return p
