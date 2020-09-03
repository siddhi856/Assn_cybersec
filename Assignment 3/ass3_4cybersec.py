def value(n):
    if(abs(100-n)<=10 or abs(200-n)<=10):
        return True
    else:
        return False
print(value(90))
print(value(104))
print(value(150))
print(value(209))
