# Find number of connected links
# and if total edges = total nodes - connected components: Acyclic

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def dfs(self, adj_list, visited, source):
        if visited[source] == 1:
            return

        visited[source] = 1  # This has to be here. Make sure you put dont put in for loop because you need to iterate through the len of adj_list[source].
        for i in adj_list[source]:
            if not visited[i]:
                self.dfs(adj_list, visited, i)

    def solve(self, A, B):
        adj_list = [[] for i in range(A + 1)]
        for i in B:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])
        count = 0
        visited = [0] * (A + 1)
        for i in range(1, len(visited)):
            if not visited[i]:
                self.dfs(adj_list, visited, i)
                count = count + 1

        e = len(B)
        if e == A - count:
            return 0, count
        return 1

if __name__ == "__main__":
    A = 3
    B = [[1, 2],[2,3]
         ]
    obj = Solution()
    print(obj.solve(A, B))
