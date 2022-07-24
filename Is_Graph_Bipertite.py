from collections import deque


class Solution:
    def isBipartite(self, graph):
        visited = [0] * len(graph)
        distance = [0] * len(graph)
        # for node in range(len(graph)):
        #     if node not in visited:
        #         visited[node] = 0
        #         q = deque()
        #         q.append(node)
        #         while q:
        #             curr = q.popleft()
        #             for adj in graph[curr]:
        #                 if adj not in visited:
        #                     visited[adj] = visited[curr]^1
        #                     q.append(adj)
        #                 elif visited[adj] == visited[curr]:
        q = deque()
        q.append(0)
        visited[0] = 1

        while q:
            u = q.popleft()
            for i in range(len(graph[u])):
                v = graph[u][i]
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
                    distance[v] = distance[u] ^ 1
        print(distance)
        q = deque()
        q.append(0)
        visited = [0] * len(graph)
        visited[0] = 1

        while q:
            u = q.popleft()
            for i in range(len(graph[u])):
                v = graph[u][i]
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
                    if distance[v] != (distance[u] ^ 1):
                        return False
        return True

        # for i in range(1, len(distance)):
        #     if distance[i] == distance[i - 1]:
        #         return False
        # return True

if __name__ == "__main__":
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    obj = Solution()
    print(obj.isBipartite(graph))
