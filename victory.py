born_pushkin = 1799        # год рождения А. С. Пушкина
born_harlamov = 1948       # год рождения Валерия Харламова
born_gogol = 1809          # год рождения Н. В. Гоголя
born_chaikovsky = 1840     # год рождения П. И. Чайковского
born_monro = 1926          # год рождения Мэрилин Монро

wish = 'да'

answer_true = 0
answer_false = 0

while  wish == 'да':
    born_pushkin_user = int(input('Введите год рождения А. С. Пушкина: '))
    if born_pushkin_user == born_pushkin:
        answer_true += 1
    else:
        answer_false += 1

    born_harlamov_user = int(input('Введите год рождения Валерия Харламова: '))
    if born_harlamov_user == born_harlamov:
        answer_true += 1
    else:
        answer_false += 1

    born_gogol_user = int(input('Введите год рождения Н. В. Гоголя: '))
    if born_gogol_user == born_gogol:
        answer_true += 1
    else:
         answer_false += 1

    born_chaikovsky_user = int(input('Введите год рождения П. И. Чайковского: '))
    if born_chaikovsky_user == born_chaikovsky:
        answer_true += 1
    else:
        answer_false += 1

    born_monro_user = int(input('Введите год рождения Мэрилин Монро: '))
    if born_monro_user == born_monro:
        answer_true += 1
    else:
        answer_false += 1
    print('Количество правильных ответов', answer_true)
    print('Количество неверных ответов', answer_false)
    print('Процент правильных ответов', int(answer_true * 100 / 5), '%')
    print('Процент неверных ответов', int(answer_false * 100 / 5), '%')

    answer_true = 0
    answer_false = 0

    wish = input('Если хотите ещё сыграть, введите да, в противном случае введите любой символ ')

print('Викторина завершена')


