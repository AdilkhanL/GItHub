import os
x = input()
y = os.path.exists(x)
if y:
    print("существует")
else:
    print("не существует")

if os.path.isabs(x):
    print("Файл")
else:
    print("Фолдер")

if os.path.islink(x):
    print("It is link")

if os.path.ismount(x):
    print("It is mount")

if os.access(x, os.R_OK):
    print("Доступ для чтение")
else:
    print("Нет доступа для чтение")
    
if os.access(x, os.W_OK):
    print("Есть доступ для записи")
else:
    print("Нет доступа для записи")

if os.access(x, os.X_OK):
    print("Есть доступ для выполнения")
else:
    print("Нет доступа для выполнения")