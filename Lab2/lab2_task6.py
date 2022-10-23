print("_______________ Вариант №1 _______________")

list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

# нумеруем список
list_num = list(enumerate(list_numbers, 0))

# находим первый max элемент с начала списка
ind,max_number = max(list_num, key=lambda i : i [1])
print(max_number)

# меняем элементы местами
list_numbers[ind], list_numbers[-1] = list_numbers[-1], list_numbers[ind]

print(list_numbers)


print("_______________Вариант №2 _______________")

list_numbers_2 = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# находим первый max элемент с начала списка

max_value = 0

for i in range(len(list_numbers_2)):
    current_value = list_numbers_2[i]
    if current_value >= max_value:
        max_value = current_value
print(max_value)

list_numbers_2[ind], list_numbers_2[-1] = list_numbers_2[-1], list_numbers_2[ind]

print(list_numbers_2)