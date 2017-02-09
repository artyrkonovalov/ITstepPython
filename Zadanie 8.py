#Запросить у пользователя 3 числа.
#a.Найти сумму первого и третьего числа.
#b.Найти произвидение суммы, которая получилась в пункте 'a' , на второе число
#
#с. Найти среднее арифметическое 3 чисел
#
#Вывести 3 числа.
#Вывести сумму
#Вывести произвидение
#Вывести среднее арифметическое 3 чисел
#
#p.s. вывод выполнить в одном print - е


firstNumber = int(input('Введите 1-е число: '))
secondNumber = int(input('Введите 2-е число: '))
thierdNumber = int(input('Введите 3-е число: '))

summaPervogoITretego = firstNumber + thierdNumber
proizvedenieSummi = summaPervogoITretego * secondNumber
sredneeArefmeticheskoe = (firstNumber + secondNumber + thierdNumber) / 3
print('Сумма 1-го и 3-го числа', summaPervogoITretego, '\nПрпоизведение 2-го числа с суммой 1-го и третьего', proizvedenieSummi, '\nСреднее арифметическое', sredneeArefmeticheskoe)
input('Нажми Ввод для продолжения...')