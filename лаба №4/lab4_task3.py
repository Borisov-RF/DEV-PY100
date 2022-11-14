...  # TODO написать функцию для получения списка уникальных целых чисел

import random

def get_unique_list_numbers() -> list[int]:
    list_ = set()
    while len(list_) <15:
        list_.add(random.randint(-10, 10))
    return (list(list_))



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
