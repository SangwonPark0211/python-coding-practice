def gcd(a,b):

    while b!=0:
        r = a%b
        a = b
        b = r
    return a

if __name__=='__main__':

    trial = int(input())
    for _ in range(trial):
        line = input().split()
        num = line[1:]
        num = [int(i) for i in num]
        sum = 0
        for i in range(int(line[0])-1):
            j=i+1
            while True:
                if j==int(line[0]):
                    break
                sum+=gcd(num[i],num[j])
                j+=1
        print(sum)