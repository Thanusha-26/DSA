class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        lf=0
        rs=sum(nums)
        n=len(nums)
        for i in range(0,n):
            if sum(nums[0:i])==sum(nums[(i+1):n]):
                return i
        return -1

