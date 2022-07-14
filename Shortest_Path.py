

class Solution:
    # @param A : Number of nodes
    # @param B : m*2 matrix where each row represents edge going from B[m][0] node to B[m][1]
    # @param s : source node
    # @param d : destination node
    # @return an integer shortest distance from s to d
    def solve(self, A, B, s, d):
        adj_list = [[] for i in range(A+1)]
        for i in B:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])
        print(adj_list)
        from collections import deque
        q = deque()
        visited = [0] * (A+1)

        q.append(s)
        visited[s] = True
        distance = 0
        while q:
            u = q.popleft()
            for i in adj_list[u]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
            distance += 1
        return distance-1

if __name__ == "__main__":
    A= 4
    B= [[1, 2],  [2, 3], [3, 4]]
    obj = Solution()
    print(obj.solve(A,B, 1, 4))


