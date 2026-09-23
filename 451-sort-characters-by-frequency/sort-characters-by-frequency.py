class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        d=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for x in d:
            ans=ans+x[0]*x[1]
        return ans