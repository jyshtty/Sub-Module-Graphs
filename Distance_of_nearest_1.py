from collections import deque


class Solution:
    def updateMatrix(self, mat):

        m, n = len(mat), len(mat[0])
        q = deque()

        # Preprocessing
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # Add all zero cells to the queue in advance
                    q.append((i, j))
                    continue
                # Set all non-zero cells to large bound value for simplifying the problem
                mat[i][j] = float('inf')

        # Updating the shortest paths with BFS
        while q:
            k = len(q)
            for i in range(k):
                r, c = q.popleft()
                # Note that the popped cell value would be the current shortest path for that cell.
                dist = mat[r][c]
                for adj_r, adj_c in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if adj_r < 0 or adj_r >= m or adj_c < 0 or adj_c >= n or mat[adj_r][adj_c] == 1:
                        continue
                    # If a new shorter distance is found for a cell, update it then
                    # enqueue the cell into queue as it might affected the shortest paths of other cells
                    # (it needs to be revisited)
                    if dist + 1 < mat[adj_r][adj_c]:
                        mat[adj_r][adj_c] = dist + 1
                        q.append((adj_r, adj_c))

        return mat