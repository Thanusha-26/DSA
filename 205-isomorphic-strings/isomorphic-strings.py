class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            # s -> t
            if a in map1:
                if map1[a] != b:
                    return False
            else:
                map1[a] = b

            # t -> s
            if b in map2:
                if map2[b] != a:
                    return False
            else:
                map2[b] = a

        return True