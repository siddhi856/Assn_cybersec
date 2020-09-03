def summer_69(arr):
    for i in range(0,len(arr)-1):
        if arr[i] == range (6,10):
            del arr[i]
        elif arr[i] != range(6,10):
            return arr[i] + arr[i + 1]

print(summer_69([1,3,5]))
