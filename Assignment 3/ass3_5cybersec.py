def has_33(n):
    for i in range(0,len(n)-1):
        if n[i:i+2]==[3,3]:
            return True
    return False
print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))
