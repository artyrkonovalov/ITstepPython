#Автобус провозит 50 пассажиров. Из них 10 едут до первой остановки, 20 - до второй, а остальные до конечной. Стоимость билетов до каждой станции соответственно равно a, b, c. Определите сколько рейсов должен делать автобус, чтобы выручка составила К руб.

cenaDlaPervoiOstanovki = int(input('Введите цену билета для поездки до 1-й остановки: '))
cenaDlaVtoroiOstanovki = int(input('Введите цену билета для поездки до 2-й остановки: '))
cenaDoKonechnoi = int(input('Введите цену билета для поездки до конечной остановки: '))
neobchodimaiaVirychka = int(input('Введите необходимую выручку: '))
virychkaZaOdinReic = (10 * cenaDlaPervoiOstanovki) + (20 * cenaDlaVtoroiOstanovki) + (20 * cenaDoKonechnoi)
neobchodimoeKolvoRecov = neobchodimaiaVirychka/virychkaZaOdinReic
print('Необходимое кол-во рейсов %s' % neobchodimoeKolvoRecov)
