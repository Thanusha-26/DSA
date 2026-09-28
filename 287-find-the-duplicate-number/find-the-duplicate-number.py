class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d={}
        for x in nums:
            if x not in d:
                d[x]=1
            else:
                d[x]=d[x]+1
        for x in d:
            if d[x]>1:
                return x