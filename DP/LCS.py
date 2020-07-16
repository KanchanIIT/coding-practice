import os

"""
Optimal Substructure:

Let the input sequences be X[0..m-1] and Y[0..n-1] of lengths m and n respectively. 
And let L(X[0..m-1], Y[0..n-1]) be the length of LCS of the two sequences X and Y.
 Following is the recursive definition of L(X[0..m-1], Y[0..n-1]).
    If last characters of both sequences match (or X[m-1] == Y[n-1]) then L(X[0..m-1], Y[0..n-1]) 
                                                        = 1 + L(X[0..m-2], Y[0..n-2])
    If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then L(X[0..m-1], Y[0..n-1]) 
                                                        = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2])

"""


class Solution:
    def __init__(self):
        self.DP = list()

    def LCS(self, s1: str, s2: str) -> int:

        # DP initiallization 2d array
        self.DP = [[0 for j in range(len(s2))] for i in range(0, len(s1))]

        if s1[0] == s2[0]:
            self.DP[0][0] = 1

        # for first row
        for row in range(1, len(s1)):
            if self.DP[row - 1][0] == 1 or s1[row] == s2[0]:
                self.DP[row][0] = 1

        # for first column
        for col in range(len(s2)):
            if self.DP[0][col - 1] == 1 or s1[0] == s2[col]:
                self.DP[0][col] = 1

        # for remaining entries
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] == s2[j]:
                    self.DP[i][j] = 1 + self.DP[i-1][j-1]
                else:
                    self.DP[i][j] = max(self.DP[i-1][j], self.DP[i][j-1])

        return self.DP[len(s1)-1][len(s2)-1]


if __name__ == "__main__":
    s = Solution()
    s1 = 'ABCDGH'
    s2 = 'AEDFHR'

    print (s.LCS(s1, s2))
