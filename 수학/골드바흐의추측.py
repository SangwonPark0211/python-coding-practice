prime = [1]*1000001
prime[0] = 0
prime[1] = 0

def goldbach(num):
    i = 3
    for i in range(3, num, 2):
        # 소수 판별
        if prime[i]==1 and prime[num-i]==1:
            print(f"{num} = {i} + {num-i}")
            return
    if i==num:
        print("Goldbach's conjecture is wrong.")
        return


def prime_flag():

    for i in range(2, 500001):
        if prime[i]==0:
            continue
        for j in range(2, 500000):
            if i*j>1000000:
                break
            prime[j*i]=0
        
if __name__=='__main__':

    prime_flag()
    while True:
        num = int(input())
        if num==0:
            break
        goldbach(num)

# 방법2)
# import sys
# #에라토스테네스의 체를 활용하여 모든 소수를 구한다.
# MAX = 1000000
# check = [False, False] + [True] * (MAX-1)
# primes = []
# count = 0
# for i in range(2, MAX+1):
#     if check[i]:
#         primes.append(i)
#         count += 1
#         for j in range(i*2, MAX+1, i):
#             check[j] = False
# # 내가 원하는 소수를 찾는 이 부분이 어려웠다.
# while True:
#     N = int(input())
# #     N = int(sys.stdin.readline())
#     if N == 0:
#         break
#     for i in range(1, count):
#         if check[N-primes[i]] == True:
#             print(f'{N} = {primes[i]} + {N-primes[i]}')
#             break


            