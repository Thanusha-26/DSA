class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq={}
        for x in words:
            if x in freq:
                freq[x]=freq[x]+1
            else:
                freq[x]=1
        arr=list(freq.keys())
        arr.sort(key=lambda x:(-freq[x],x))
        return arr[:k]