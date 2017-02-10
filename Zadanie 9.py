#На концерте певицы было А % отдыхающих в санатории, на выступление хора зрителей собралось в 1,5 раза больше. Сколько зрителей побывало на этих концертах в общем, если всего в санатории отдыхало х человек.

lydVSanatorii = int(input('Введите кол-во людей в санатории: '))
procent = int(input('Введите процент людей посетивших концерт: '))
lydNaSvistoplaske = (lydVSanatorii * procent)/100
lydNaHorePravoslavnom = lydNaSvistoplaske * 1.5
obshiiLydNaHorePravoslavnomISvistoplaske = lydNaHorePravoslavnom + lydNaSvistoplaske
print('Общее кол-во людей поситившие мероприятия %s' % obshiiLydNaHorePravoslavnomISvistoplaske)
input('Нажми Ввод для продолжения...')