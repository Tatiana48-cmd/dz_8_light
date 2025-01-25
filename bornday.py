born_pushkin = 1799
dayborn_pushkin = '06 июня'

born_pushkin_user = int(input('Введите год рождения А. С. Пушкина: '))

if born_pushkin_user == born_pushkin:
    dayborn_pushkin_user = input('Введите день рождения А. С. Пушкина в формате: ДД название месяца ')
    if dayborn_pushkin_user == dayborn_pushkin:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')

