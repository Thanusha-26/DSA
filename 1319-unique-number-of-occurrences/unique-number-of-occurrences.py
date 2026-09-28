class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq={}
        for x in arr:
            freq[x]=freq.get(x,0)+1
        l=list(freq.values())
        if len(l)==len(set(l)):
            return True
        else:
            return False