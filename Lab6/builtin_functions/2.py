string = input()
u_c = 0
l_c = 0
for i in range(len(string)):
    if string[i] >= chr(65) and string[i] <= chr(90):
        u_c = u_c + 1
    if string[i] >= chr(97) and string[i] <= chr(122):
        l_c = l_c + 1
print(u_c)
print(l_c)