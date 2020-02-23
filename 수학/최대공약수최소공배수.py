num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
gcd = 1
lcm = 1
div = 2
while True:
    smaller = min(num1, num2)
    if div > smaller:
        break
    if num1 % div == 0 and num2 % div == 0:
        num1 = num1//div
        num2 = num2//div
        gcd *= div
        div = 1
    div += 1
lcm = gcd * num1 * num2
print(gcd)
print(lcm)    

# 방법 1) import math 후 math.gcd(a,b)이용
# 방법 2) https://suri78.tistory.com/36 (유클리드 호제법)