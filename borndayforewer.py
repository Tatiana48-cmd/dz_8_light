born_pushkin = 1799
dayborn_pushkin = '06 июня'

born_pushkin_user = None
dayborn_pushkin_user = None


while born_pushkin_user != born_pushkin:
    born_pushkin_user = int(input('Введите год рождения А. С. Пушкина: '))

if born_pushkin_user == born_pushkin:

    while dayborn_pushkin_user != dayborn_pushkin:
        dayborn_pushkin_user = input('Введите день рождения А. С. Пушкина в формате: ДД месяц ')

print('Верно')


