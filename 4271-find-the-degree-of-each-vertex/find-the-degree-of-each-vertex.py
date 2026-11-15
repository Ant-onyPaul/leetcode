class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        a=0
        c=[]*len(matrix)
        for i in range(len(matrix)):
            b=sum(matrix[i])
            c.append(b)
        return c



        