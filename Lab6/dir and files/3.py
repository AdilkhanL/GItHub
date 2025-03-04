import os
x = input()
if os.path.exists(x):
    print("Существует")
    d = os.path.dirname(x)
    b = os.path.basename(x)
    print("Путь до файл: ", d)
    print("Имя файла: ", b)
else:
    print("Не существует")