class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l=[int(i) for i in str(n)]
        o=0
        e=0
        for j in range(len(l)):
            if j%2==0:
                e=e+l[j]
            else:
                o=o+l[j]
        return e-o