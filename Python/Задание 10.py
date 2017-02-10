'''Автобус провозит 50 пассажиров. Из них 10 едут до первой остановки,
20 - до второй, а остальные до конечной.
Стоимость билетов до каждой станции соответственно равно.
Определите сколько рейсов должен делать автобус,
чтобы выручка составила К руб.'''

priceDlaPervoiOstanovki = int(input('Введите цену билета для поездки до 1-й остановки: '))
priceDlaVtoroiOstanovki = int(input('Введите цену билета для поездки до 2-й остановки: '))
priceDoKonechnoi = int(input('Введите цену билета для поездки до конечной остановки: '))
neobchodimaiaVirychka = int(input('Введите необходимую выручку: '))
virychkaZaOdinReic = (10 * priceDlaPervoiOstanovki) +(20 * priceDlaVtoroiOstanovki) + (20 * priceDoKonechnoi)
neobchodimoeKolvoRecov = neobchodimaiaVirychka/virychkaZaOdinReic
print('Необходимое кол-во рейсов %s' % neobchodimoeKolvoRecov)

input("Press Enter to continue...")
