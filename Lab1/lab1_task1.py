list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
un_num = set(list_)

sum_unik_chisel_ = sum(un_num)
len_ = len(un_num)

sr_arif_un_chisel = round((sum_unik_chisel_ / len_), 5)

print(sum_unik_chisel_)
print(len_)
print(sr_arif_un_chisel)