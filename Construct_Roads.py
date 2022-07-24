class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = [[] for i in range(A+1)]
        indegree = [0 for i in range(A + 1)]

        for i in B:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            indegree[i[0]] += 1
            indegree[i[1]] += 1


        from collections import deque
        q = deque()
        visited = [0 for i in range(A + 1)]
        distance = [0 for i in range(A + 1)]

        # for i in range(len(indegree)):
        #     if indegree[i] == 1:
        #         q.append(i)
        q.append(8)
        visited[1] = 1

        while q:
            u = q.popleft()
            for i in range(len(graph[u])):
                v = graph[u][i]
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
                    distance[v] = distance[u] + 1
        n = max(distance)
        if n == 1 or n == 2:
            return 0
        if n % 2 == 0:
            n = n - 1

        nodes = n + 1
        color = nodes // 2

        totol_edges = color * color

        requried_edges = totol_edges - n
        return requried_edges, distance

if __name__ == "__main__":
    A =  15
    # B = [[1,2], [2,3], [4,3]]
    B = [
  [7, 5],
  [15, 14],
  [11, 2],
  [8, 7],
  [10, 3],
  [5, 3],
  [4, 2],
  [6, 4],
  [13, 2],
  [3, 2],
  [14, 11],
  [12, 9],
  [2, 1],
  [9, 2],
]
    obj = Solution()
    print(obj.solve(A, B))