import os

# Название папки, которую хотим создать
folder = "my folder"

# Создаём папку, если она ещё не существует
os.makedirs(folder, exist_ok=True)

# Создаём несколько текстовых файлов внутри этой папки
for i in range(26):
    file_path = os.path.join(folder, f"{chr(i + 65)}.txt")
    with open(file_path, "w") as file:
        file.write(f"file {i + 1}")