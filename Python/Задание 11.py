'''N человек снимают квартиры на лето. 50% из них живет неделю, 40% - 15 дней,
а остальные по 20 дней. Оплата проживания за 1 день равна х руб.
Сколько налогов заплатят хозяева, если они составляют 13% от всей выручки.'''


manInHourse = int(input('Введиет кол-во проживающих в квартире: '))
manInOneWeek = manInHourse / 0.5
manIn15Days = manInHourse / 0.4
other = manInHourse / 0.1

cost_ofOneDay = int(input('Введиет стоимость дня в квартире: '))

sumBehindOneMonth = ((manInOneWeek * (7 * cost_ofOneDay)) + (manIn15Days * (15 * cost_ofOneDay)) + (other * (20 * cost_ofOneDay))) *13
print('Налоги: %s' % sumBehindOneMonth)





input("Press Enter to continue...")
