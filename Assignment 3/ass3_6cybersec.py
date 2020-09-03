def blackjack(nums):
    sum=0
    for i in range(0,3):
        sum=sum+nums[i]
    if(sum<=21):
        return sum
    elif(sum>21 and 11 in nums):
        return sum-10
    else:
        return 'BUST'
print(blackjack((5,6,9)))
print(blackjack((9,9,9)))
print(blackjack((9,9,11)))
        
