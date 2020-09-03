def count_prime(n):
    count=0
    for i in range(2,n+1):
        value=True
        for j in range(2,i):
            if(i%j==0):
                value=False
                break
        if value:
            count=count+1
    return count
print("Enter a number")
n=int(input())
print(count_prime(n))
