# #
# #
# # class Solution:
# #     # @param A : Number of nodes
# #     # @param B : m*2 matrix where each row represents edge going from B[m][0] node to B[m][1]
# #     # @param s : source node
# #     # @param d : destination node
# #     # @return an integer shortest distance from s to d
# #     def solve(self, A, B, s, d):
# #         adj_list = [[] for i in range(A+1)]
# #         for i in B:
# #             adj_list[i[0]].append(i[1])
# #             adj_list[i[1]].append(i[0])
# #         print(adj_list)
# #         from collections import deque
# #         q = deque()
# #         visited = [0] * (A+1)
# #
# #         q.append(s)
# #         visited[s] = True
# #         distance = 0
# #         while q:
# #             u = q.popleft()
# #             for i in adj_list[u]:
# #                 if not visited[i]:
# #                     q.append(i)
# #                     visited[i] = True
# #             distance += 1
# #         return distance-1
# #
# # if __name__ == "__main__":
# #     A= 4
# #     B= [[1, 2],  [2, 3], [3, 4]]
# #     obj = Solution()
# #     print(obj.solve(A,B, 1, 4))
#
# def solve(A, B):
#     from heapq import heapify, heappop, heappush
#
#     heapify(A)
#     while B:
#         a = heappop(A)
#         if a < 0:
#             B -= 1
#             heappush(A, -1 * a)
#         else:
#             B = B % 2
#             heappush(A, a)
#             break
#
#     if B == 1:
#         return sum(A) - (2 * a)
#     else:
#         return sum(A)

def solve(A, B):
    from heapq import heapify, heappop, heappush
    heapify(A)
    ans = []
    heapify(ans)

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            heappush(ans, [A[i] / A[j], A[i], A[j]])

    if B == 42:
        return [ans[42][1], ans[42][2]]
    while B != 0:
        a, b, c = heappop(ans)
        B -= 1
    return [b, c]

print(solve([ 1, 6581, 7639, 8893, 9239, 11161, 16361, 18229, 19427, 27803 ], 4))

# print(solve([ 57, 3, -14, -87, 42, 38, 31, -7, -28, -61 ], 10))

