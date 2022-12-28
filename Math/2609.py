A,B= map(int,input().split())
if(A==1):
    print(1)
    print(B)
elif(B==1):
    print(1)
    print(A)
else:
    i = min(A,B)
    while(1):
        if(A%i==0 and B%i==0):
            gcd = i
            print(gcd)
            break
        i -= 1
    i = 1
    while(1):
        if((A*i)%B == 0):
            lcm = A*i
            print(lcm)
            break
        i += 1
