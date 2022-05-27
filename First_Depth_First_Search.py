class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        adj_list = [[] for i in range(len(A)+1)]
        for i in range(1, len(A)):
            adj_list[A[i]].append(i + 1 )


        visited = [0] * (len(A)+1)

        from collections import deque
        q = deque()
        q.append(C)

        visited[C] = 1

        while q:
            v = q.popleft()
            for i in adj_list[v]:
                if i == B:
                    return 1
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
        return visited[B]

if __name__ == "__main__":
    A= [ 1, 1, 1, 3, 3, 2, 2, 7, 6 ]
    B= 9
    C= 1
    obj = Solution()
    print(obj.solve(A, B, C))
