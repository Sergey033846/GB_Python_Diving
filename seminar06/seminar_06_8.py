# Задание №8
# Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# - Какие вещи взяли все три друга (что конкретно подразумевается?)
# - Какие вещи уникальны, есть только у одного друга
# - Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

dict1 = {'Вася': ('фонарь', 'спички'),
         'Петя': ('фонарь', 'мангал', 'палатка'),
         'Коля': ('фонарь', 'спички', 'палатка'),
         'Женя': ('фонарь', 'топор', 'палатка', 'спички'),  # первым был фонарь
         # 'Женя': ('топор', 'палатка', 'спички'),  # первым был фонарь
         'Иван': ('фонарь', 'кетчуп', 'палатка', 'спички')
         }

# на случай, если придется делать со словарем
# # формируем словарь 'вещь: друзья':
# dict_things = dict()
# for friend, things in dict1.items():
#     for thing in things:
#         if thing not in dict_things:
#             dict_things[thing] = {friend}
#         else:
#             dict_things[thing].add(friend)
#
# # формируем список друзей
# list_friends = {friend for friend in dict1}

# Отвечаем на вопросы:
# - Какие вещи взяли все три друга (что конкретно подразумевается?):

set_all_intersection = set()
flag_first_iteration = True

for friend, things in dict1.items():
    friend_things = set(things)

    if flag_first_iteration:
        set_all_intersection = friend_things
        flag_first_iteration = False
    else:
        set_all_intersection = set_all_intersection.intersection(friend_things)

print(f'Какие вещи взяли все три друга (пересечение): {set_all_intersection}')
print()

# - Какие вещи уникальны, есть только у одного друга:

print('Какие вещи уникальны, есть только у одного друга:')

for friend, things in dict1.items():
    unique_friend_things = set(things)

    for other_friend, other_things in dict1.items():
        if friend != other_friend:
            unique_friend_things = unique_friend_things - set(other_things)

    print(friend, unique_friend_things)

# - Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует:

print()
print('Какие вещи есть у всех друзей, кроме одного, и имя того, у кого данная вещь отсутствует:')

for friend, things in dict1.items():
    set_all_intersection_others = set()
    flag_first_iteration = True

    for other_friend, other_things in dict1.items():
        if friend != other_friend:
            other_friends_things = set(other_things)
            if flag_first_iteration:
                set_all_intersection_others = other_friends_things
                flag_first_iteration = False
            else:
                set_all_intersection_others = set_all_intersection_others.intersection(other_friends_things)

    print(friend, set_all_intersection_others - set(things))

# ai
#
# friends = {
#     'Иван': ['палатка', 'спальник', 'фонарик', 'книга'],
#     'Мария': ['спальник', 'фонарик', 'карта', 'компас'],
#     'Петр': ['палатка', 'спальник', 'книга', 'аптечка']
# }
#
# # Вещи, которые взяли все три друга
# common_items = set(friends['Иван']) & set(friends['Мария']) & set(friends['Петр'])
#
# # Уникальные вещи, которые взял только один друг
# unique_items = {
#     friend: set(items) - (set(friends['Мария']) | set(friends['Петр']) | set(other_items))
#     for friend, items in friends.items()
#     for other_friend, other_items in friends.items()
#     if friend != other_friend
# }
#
# # Вещи, которые есть у всех друзей, кроме одного, и имя того, у кого вещь отсутствует
# almost_common_items = {}
# for item in friends[list(friends.keys())[0]]:
#     has_item = [name for name in friends if item in friends[name]]
#     missing_friend = None
#     if has_item:
#         try:
#             missing_friend = (set(friends.keys()) - set(has_item)).pop()
#         except KeyError:
#             pass
#     if len(has_item) == len(friends) - 1:
#         almost_common_items[item] = missing_friend
#
# print("Вещи, которые взяли все три друга:", common_items)
# print("Уникальные вещи:")
# for name, items in unique_items.items():
#     print(f"У {name}: {items}")
# print("Вещи, которые есть у всех друзей, кроме одного, и имя того, у кого вещь отсутствует:")
# for item, friend in almost_common_items.items():
#     print(f"{item} отсутствует у {friend}")
