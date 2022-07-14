class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers

    def solve(self, A, B):
        indegree = [0] * (A + 1)
        indegree[0] = float("inf")
        adj = [[0] for i in range((A + 1))]
        for i in B:
            adj[i[0]].append(i[1])
            indegree[i[1]] += 1

        from collections import deque
        from heapq import heapify, heappush, heappop
        q = []
        heapify(q)

        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                heappush(q, i)
        ans = []
        while q:
            v = heappop(q)
            ans.append(v)
            for i in adj[v]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    heappush(q, i)
        return ans

if __name__ == "__main__":
    A = 8
    B = [ [1, 4],
  [1, 2],
  [4, 2],
  [4, 3],
  [3, 2],
  [5, 2],
  [3, 5],
  [8, 2],
  [8, 6]]
    obj = Solution()
    print(obj.solve(A, B))
    # 1 4 3 5 7 8 2 6