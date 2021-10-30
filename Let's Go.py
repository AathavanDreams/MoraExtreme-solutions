n=int(input())
if 2<=n<=20:
    for i in range(n-1):
        print(end="  ")
        print ((n-1)*"* ")
    for i in range(n+1,0,-1):
        print((n+1-i)*" ",end="")
        print(i*"* ")
