# https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        total = 0
        rotten = 0
        from collections import deque
        q = deque()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 or A[i][j] == 2:
                    total += 1
                if A[i][j] == 2:
                    rotten += 1
                    q.append([i,j])
        l = len(A)
        b = len(A[0])
        time = 0
        q.append([100,100])
        while q and len(q) > 1:
            x,y = q.popleft()
            if x == 100 and y == 100:
                time += 1
                q.append([100, 100])
                continue
            if x>0 and A[x-1][y] == 1:
                A[x-1][y] = 2
                rotten += 1
                q.append([x-1, y])
            if y >0 and A[x][y-1] == 1:
                A[x][y-1] = 2
                rotten += 1
                q.append([x, y-1])
            if x < l - 1 and A[x+1][y] == 1:
                A[x+1][y] = 2
                rotten += 1
                q.append([x+1, y])
            if y < b - 1 and A[x][y+1] == 1:
                A[x][y+1] = 2
                rotten += 1
                q.append([x, y+1])

        if total == rotten:
            return time
        return -1

if __name__ == "__main__":
    A = [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1]]
    obj = Solution()
    print(obj.solve(A))
