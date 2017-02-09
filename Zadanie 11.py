#N человек снимают квартиры на лето. 50% из них живет неделю, 40% - 15 дней, а остальные по 20 дней. Оплата проживания за 1 день равна х руб. Сколько налогов заплатят хозяева, если они составляют 13% от всей выручки.

lydiVKvartire = int(input('Введиет кол-во проживающих в квартире: '))
teKtoNaOdnyNedely = lydiVKvartire / 0.5
teKtoNa15Dnei = lydiVKvartire / 0.4
ostalnie = lydiVKvartire / 0.1

stoimostZaOdinDen = int(input('Введиет стоимость дня в квартире: '))

summaZaMecac = ((teKtoNaOdnyNedely * (7 * stoimostZaOdinDen)) + (teKtoNa15Dnei * (15 * stoimostZaOdinDen)) + (ostalnie * (20 * stoimostZaOdinDen))) *1 0.13
print('Налоги: %s' % summaZaMecac)
