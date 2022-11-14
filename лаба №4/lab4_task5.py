# TODO написать функцию генерации случайных паролей

from string import *
from random import *

i = 8   # количество символов в пароле

def get_random_password(i) -> str:
    sample_ = sample(ascii_letters + digits, i)
    return "".join(sample_)


print(get_random_password(i))
