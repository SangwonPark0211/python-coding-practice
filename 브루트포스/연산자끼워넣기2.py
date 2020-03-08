# from itertools import permutations
# import sys

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# plus, minus, multiple, division = map(int, sys.stdin.readline().split())

# operation_list = []
# operation_list += [1]*plus
# operation_list += [2]*minus
# operation_list += [3]*multiple
# operation_list += [4]*division

# operation_set = []
# operation_set = list(set(permutations(operation_list, N-1)))

# max_answer = -1000000001
# min_answer = 1000000001
# for case in operation_set:
#     answer = A[0]

#     for i in range(N-1):
#         if case[i] == 1:
#             answer += A[i+1]
#         elif case[i] == 2:
#             answer -= A[i+1]
#         elif case[i] == 3:
#             answer *= A[i+1]
#         else:
#             if answer<0:
#                 answer = -(-answer//A[i+1])
#             else:
#                 answer //= A[i+1]
    
#     if answer<min_answer:
#         min_answer = answer
#     if answer>max_answer:
#         max_answer = answer

# print(max_answer)
# print(min_answer)


# 출처 : https://statssy.github.io/pro/2019/09/11/baekjoon_15658/
n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
mx, mn = -1e9, 1e9 # 최대 최소 처음 수

def solve(index, ans, add, sub, mul, div) :
    global mx, mn
    if index >= n :
        mx = max(mx, ans)
        mn = min(mn, ans)
        return
    if add > 0 :
        solve(index+1, ans+a[index], add-1, sub, mul, div)
    if sub > 0 :
        solve(index+1, ans-a[index], add, sub-1, mul, div)
    if mul > 0 :
        solve(index+1, ans*a[index], add, sub, mul-1, div)
    if div > 0 :
        solve(index+1, ans//a[index] if ans > 0 else -((-ans)//a[index]), add, sub, mul, div-1)

solve(1, a[0], op[0], op[1], op[2], op[3])
print(mx)
print(mn)
