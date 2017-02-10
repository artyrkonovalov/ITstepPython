'''На концерте певицы было А % отдыхающих в санатории,
на выступление хора зрителей собралось в 1,5 раза больше.
Сколько зрителей побывало на этих концертах в общем,
если всего в санатории отдыхало х человек.'''


manInSanatori = int(input('Введите кол-во людей в санатории: '))
procent = int(input('Введите процент людей посетивших концерт: '))
manInKoncert = (manInSanatori * procent)/100
manNaSongs = manInKoncert * 1.5
obshiimanNaSongIKoncerte = manNaSongs + manInKoncert
print('Общее кол-во людей поситившие мероприятия %s' % obshiimanNaSongIKoncerte)

input("Press Enter to continue...")
