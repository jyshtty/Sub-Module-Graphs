# (i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
# (i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
# (i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
# (i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
# (i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
# (i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
# (i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
# (i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
def isSafe(i, j):
    # row number is in range, column number
    # is in range and value is 1
    # and not yet visited
    return (i >= 0 and i < len(A) and
            j >= 0 and j < len(A[0]) and A[i][j])


def dfs(A, i, j):

    p = [-1, -1, 0, 1, 1, 1, 0, -1]
    q = [0, 1, 1, 1, 0, -1, -1, -1]

    for each in range(8):
        if isSafe(i + p[each], j + q[each]):
            A[i + p[each]][j + q[each]] = 0
            dfs(A, i + p[each], j + q[each])

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    A[i][j] = 0
                    count += 1
                    dfs(A, i, j)
        return count, A

if __name__ == "__main__":
    A = [[0, 0, 1, 0, 1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1, 1, 1, 0, 1]]
    obj = Solution()
    print(obj.solve(A))
