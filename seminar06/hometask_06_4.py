# Cписок повторяющихся элементов
#
# Дан список повторяющихся элементов lst.
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
#
# На входе:
# lst = [1, 1, 2, 2, 3, 3]
#
# На выходе:
# [1, 2, 3]

lst = [1, 1, 2, 2, 5, 3, 3, 4]

set1 = set()

for item in lst:
    if lst.count(item) > 1:
        set1.add(item)
print(list(set1))

# решение автотеста
# duplicates = set()
#
# for item in lst:
#     if lst.count(item) >= 2:
#         duplicates.add(item)
#
# result = list(duplicates)
# print(result)
