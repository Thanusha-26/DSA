class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s=0
        for i in range(len(mat)):
            s=s+mat[i][i]
        for i in range(len(mat)):
            s=s+mat[i][len(mat)-i-1]
        if len(mat)%2==0:
            return s
        else:
            return s-mat[len(mat)//2][len(mat)//2]
        