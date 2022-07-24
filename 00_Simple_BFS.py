class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def solve(self, A, B):
        visited = [0 for i in range(A + 1)]
        graph = [[] for i in range(A + 1)]
        for i in B:
            graph[i[0]].append(i[1])

        from collections import deque
        q = deque()
        visited[1] = 1

        q.append(1)
        while q:
            u = q.popleft()
            for i in range(len(graph[u])):
                v = graph[u][i]
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
        return visited[A]
# from collections import Counter, deque
#
#
# class Solution:
#     # @param A : string
#     # @return a strings
#
#     def solve(self, A):
#         if len(A) == 0:
#             return ""
#         ans = A[0]
#         d = Counter(A)
#         start = 0
#         ans_len = 0
#         q = deque()
#         q.append(A[0])
#         l = len(A)
#         for i in range(1, l):
#
#             ch = A[i]
#
#             if ch not in d:
#                 d[ch] = 0
#             if d[ch] > 1:
#                 try:
#                     q.remove(ch)
#                 except:
#                     pass
#
#                 d[ch] -= 1
#             elif d[ch] == 1:
#                 q.append(ch)
#
#             if not q:
#                 ans += "#"
#             else:
#                 ans += q[0]
#
#             # print("i: " + str(i) + " start: " + str(start) + " ans: " + str(ans))
#
#         return ans
#             # , q, Counter(A),
#
# if __name__ == "__main__":
#     A = "jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"
#     obj = Solution()
#     print(obj.solve(A))


def minPathSum(grid):
    m = len(grid)  # row
    n = len(grid[0])  # column

    dp = [[-1 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[0][0] = grid[0][0]
            elif i == 0:
                dp[0][j] = dp[0][j - 1] + grid[0][j]
            elif j == 0:
                dp[i][0] = dp[i - 1][j] + grid[i][0]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m-1][n - 1]

print(minPathSum([[1,2,3],[4,5,6]]))