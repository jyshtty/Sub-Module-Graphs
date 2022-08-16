# Undirected weighted graph
# shortest distance with minimum weight



class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        graph = [[] for i in range(A)]

        for i in B:
            graph[i[0]].append([i[1], i[2]])
            graph[i[1]].append([i[0], i[2]])

        distance = [float("inf") for i in range(A)]

        from heapq import heapify, heappush, heappop
        q = []
        heapify(q)

        heappush(q, [0, C])
        distance[C] = 0
        while q:
            u = heappop(q)
            d = u[0]
            n = u[1]

            if d == distance[n]:
                for i in range(len(graph[n])):
                    v = graph[n][i]
                    node = v[0]
                    weight = v[1]
                    if distance[n] + v[1] < distance[node]:
                        distance[node] = distance[n] + v[1]
                        heappush(q, [distance[node], node])
        for i in range(len(distance)):
            if distance[i] == float("inf"):
                distance[i] = -1

        return distance

if __name__ == "__main__":
    obj = Solution()
    A = 6
    B =[
        [0, 4, 9],
        [3, 4, 6],
        [1, 2, 1],
        [2, 5, 1],
        [2, 4, 5],
        [0, 3, 7],
        [0, 1, 1],
        [4, 5, 7],
        [0, 5, 1]
    ]
    C= 4
print(obj.solve(A, B, C))
