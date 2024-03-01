# Завдання 1

# Змінній var_int надайте значення 10, var_float – значення 8.4, var_str – "No".
var_int = 10
var_float = 8.4
var_str = "No"

# Змініть значення, збережене в змінній var_int, збільшивши його в 3.5 рази, результат зв'яжіть зі змінною big_int.
big_int = var_int * 3.5

# Змініть значення, збережене в зміній var_float, зменшивши його на одиницю, результат зв'яжіть з тієї ж змінною.
var_float -= 1

# Розділіть var_int на var_float, а потім big_int на var_float. Результат даних виразів не прив'язуйте до жодних змінних.
var_int / var_float
big_int / var_float

# Змініть значення змінної var_str на "NoNoYesYesYes". При формуванні нового значення використовуйте операції конкатенації (+) і повторення рядка (*).
var_str = "No" * 2 + "Yes" * 4

# Виведіть значення всіх змінних.
print("var_int:", var_int)
print("var_float:", var_float)
print("var_str:", var_str)
print("big_int:", big_int)

# Завдання 2

# Введення даних
a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))
d = int(input("Введіть d: "))

# Обчислення Y
y_c = 5 * math.sqrt(c + 1) + a**2 - b**2
y_d = 5 * math.sqrt(d + 1) + a**2 - b**2

# Виведення результатів
print("Y для x = c:", y_c)
print("Y для x = d:", y_d)