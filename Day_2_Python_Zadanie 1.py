'''Запросить у пользователя 3 числа.
	a.Найти сумму первого и третьего числа.
	b.Найти произвидение суммы, которая получилась в пункте 'a' , на второе число
	с. Найти среднее арифметическое 3 чисел
		
		Вывести 3 числа.
		Вывести сумму
		Вывести произвидение
		Вывести среднее арифметическое 3 чисел
		p.s. вывод выполнить в одном print - е '''




firstNumber = int(input("Ввести первое число = "))
secondNumber = int(input("Ввести второе число = "))
thirdNumber = int(input("Ввести третье число = "))
print('Первое число =  \n',firstNumber)
print('Второе число =  \n',secondNumber)
print('ТРетье число =  \n',thirdNumber)
summaFistAndThird = firstNumber + thirdNumber
proizvedenieSummi = summaFistAndThird * secondNumber
sredneeArefmeticheskoe = (firstNumber + secondNumber + thirdNumber) / 3
print('Сумма 1-го и 3-го числа =  ', summaFistAndThird,
      '\nПрпоизведение 2-го числа с суммой 1-го и 3-его = ',proizvedenieSummi,
         '\nСреднее арифметическое =  ',sredneeArefmeticheskoe)



input("Press Enter to continue...")
