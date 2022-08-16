

from collections import deque
class Solution:
    def solve(self, A, B):
        graph = [[] for i in range(A)]
        for i in B:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        color = [0 for i in range(A)]
        q = deque()

        for i in range(A):
            if color[i] == 0:
                q.append(i)
                color[i] = 1
            while q:
                u = q.popleft()
                for i in range(len(graph[u])):
                    v = graph[u][i]
                    if color[v] == 0:
                        color[v] = 3 - color[u] # all the edges you will color the opposite color. if color[u] = 2, color[v] = 1 lly if color[u] = 1, color [v] = 2. ytherefor color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return 0
        return 1

if __name__ == "__main__":
    A = 94
    B = [
      [10, 82],
      [43, 64],
      [24, 56],
      [35, 66],
      [44, 70],
      [7, 27],
      [29, 82],
      [1, 86],
      [5, 27],
      [68, 82],
      [5, 41],
      [36, 64],
      [0, 38],
      [30, 92],
      [51, 88],
      [12, 52],
      [45, 59],
      [40, 41],
      [17, 28],
      [43, 46],
      [22, 62],
      [17, 25],
      [38, 91],
      [44, 74],
      [26, 57],
      [27, 88],
      [57, 68],
      [19, 76],
      [63, 85],
      [32, 36],
      [3, 50],
      [42, 71],
      [44, 75],
      [56, 92],
      [23, 47],
      [40, 93],
      [56, 59],
      [24, 51],
      [46, 68],
      [32, 90],
      [25, 37],
      [26, 92],
      [3, 9],
      [76, 90],
      [68, 93],
      [34, 48],
      [53, 71],
      [15, 79],
      [10, 37],
      [13, 66],
      [66, 79],
      [17, 26],
      [3, 41],
      [45, 57],
      [73, 92],
      [14, 28],
      [67, 92],
      [33, 39],
      [25, 63],
      [20, 71],
      [22, 29],
      [33, 49],
      [9, 41],
      [26, 80],
]
    obj = Solution()
    print(obj.solve(A, B))
