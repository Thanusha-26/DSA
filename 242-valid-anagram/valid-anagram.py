class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t) or set(s)!=set(t):
            return False
        else:
            d={}
            for ch in s:
                if ch in d:
                    d[ch]=d[ch]+1
                else:
                    d[ch]=1
            for ch in t:
                if ch in d:
                    d[ch]=d[ch]-1
                else:
                    return False
                if d[ch]==0:
                    del d[ch]
            return len(d)==0