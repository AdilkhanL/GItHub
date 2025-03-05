import time
import math

# Ввод данных от пользователя
number, delay = map(int, input("Введите число и задержку в миллисекундах (например: 25100 2123): ").split())

# Задержка в миллисекундах (переводим в секунды)
time.sleep(delay / 1000)

# Вычисляем квадратный корень
sqrt_result = math.sqrt(number)

# Выводим результат
print(f"Квадратный корень из {number} через {delay} миллисекунды равен {sqrt_result}")