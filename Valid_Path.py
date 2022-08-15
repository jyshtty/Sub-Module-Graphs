import math
import queue

def dfs(A, B, C, D, E, F, x,y, boo):
    boo[y][x] = 1
    nei_x = [-1,0,1,-1,1,-1,0,1]
    nei_y = [1,1,1,0,0,-1,-1,-1]
    for nei in range(8):
        va1 = x+nei_x[nei]
        va2 = y+nei_y[nei]
        bo = False
        if 0<=va1<=A and 0<=va2<=B:
            for cir in range(C):
                va_1 = (va1-E[cir])*(va1-E[cir])
                va_2 = (va2-F[cir])*(va2-F[cir])
                if va_1+va_2 <= (D*D):
                    bo = True
            if bo==True:
                boo[va2][va1] = -1
            if boo[va2][va1] == 0:
                dfs(A, B, C, D, E, F, va1,va2, boo)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        boo = [[0 for k in range(A+1)] for i in range(B+1)]
        dfs(A, B, C, D, E, F, 0,0, boo)
        if boo[B][A] == 1:
            return "YES"
        return 'NO'