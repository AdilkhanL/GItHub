'''
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
'''
'''
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.readline(4))
'''
'''
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
'''
my_list = input("Введите лист:").split()
print(my_list)
my_list = [item.strip() for item in my_list]
with open("output.txt","w") as file:
    for item in my_list:
        file.write(item + "\n")
print("Все готово")