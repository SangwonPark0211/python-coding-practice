from itertools import permutations
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
plus, minus, multiple, division = map(int, sys.stdin.readline().split())

operation_list = []
operation_list += [1]*plus
operation_list += [2]*minus
operation_list += [3]*multiple
operation_list += [4]*division

operation_set = []
operation_set = list(set(permutations(operation_list, N-1)))

max_answer = -1000000001
min_answer = 1000000001
for case in operation_set:
    answer = A[0]

    for i in range(N-1):
        if case[i] == 1:
            answer += A[i+1]
        elif case[i] == 2:
            answer -= A[i+1]
        elif case[i] == 3:
            answer *= A[i+1]
        else:
            if answer<0:
                answer = -(-answer//A[i+1])
            else:
                answer //= A[i+1]
    
    if answer<min_answer:
        min_answer = answer
    if answer>max_answer:
        max_answer = answer

print(max_answer)
print(min_answer)