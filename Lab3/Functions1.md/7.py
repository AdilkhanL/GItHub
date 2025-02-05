'''
n = int(input("Nimber of lists: "))
#list(n)
for i in range(n):
    list1 = input().split()
    list1 = list(map(int, list1))
    print(list1)
    i = i + 1
print(list1)
'''

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1 ,3]))
print(has_33([3, 1, 3]))