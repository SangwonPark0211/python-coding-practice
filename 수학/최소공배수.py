#방법1)lcm = gcd * (a//gcd) * (b//gcd) 이용
# def gcd(a,b):

#     if a==0:
#         return b
#     elif b==0:
#         return a

#     if a>b:
#         a %= b
#         return gcd(a,b)
#     else:
#         b %= a
#         return gcd(a,b)
        
# if __name__ == '__main__':
#     trial = int(input())
#     for i in range(trial):
#         a, b = map(int, input().split())
#         result = gcd(a,b)
#         result *= (a//result) * (b//result)
#         print(result)

#방법2) lcm = A*B//gcd 이용
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    #기존의 값을 복사해둠
    x = a
    y = b
    # a, b 중 뭐가 큰지 나누지 않아도 노상관
    # Ex) gcd(18,24)=gcd(24,18)처럼 되므로 
    while b != 0:
        r = a % b
        a = b
        b = r
    gcd = a
    lcd = x * y // a
    print(lcd)