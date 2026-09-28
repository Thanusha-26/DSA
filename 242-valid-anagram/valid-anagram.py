class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t) or set(s)!=set(t):
            return False
        else:
            for ch in set(s):
                if s.count(ch)!=t.count(ch):
                    return False
            return True