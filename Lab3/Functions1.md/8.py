def spy_game(nums):
    kereksan = [0, 0, 7]
    q = 0
    for i in nums:
        if i == kereksan[q]:
            q +=1
        if q == len(kereksan):
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))