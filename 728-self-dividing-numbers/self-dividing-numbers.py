class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left,right+1):
            n=i
            valid=True
            while(n>0):
                r=n%10
                if r==0 or i%r!=0:
                    valid=False
                    break
                n=n//10
            if valid:
                l.append(i)
        return l