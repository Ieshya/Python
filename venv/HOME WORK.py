# EASY

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


# fruit=['яблоко','банан','груша','слива','апельсин','персик','киви']
# right_o = len(max(fruit, key = len))
# for index, item  in enumerate(fruit, start=1):
#     print('{}.{}'.format(index, item.rjust(right_o)))





# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


# a=[1,2,3,4,5,6]
# b=[9,8,7,6,5,4]
# for list_a in b:
#     if list_a in a:
#         a.remove(list_a)
# print(a)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# b=[]
# for i in a:
#     if i%2 == 0:
#         b.append(i/4)
#     else:
#         b.append(i*2)
# print(b)

# NORMAL
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# b=[]
# for i in a:
#     if i > 0 and i**0.5%1==0:
#         b.append(int(i**0.5))
# print(b)



# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# data = '05.12.2000'
# dict_day={'01':'Первое',
#           '02':'Второе',
#           '03':'Третье',
#           '04':'Четвертое',
#           '05':'Пятое',
#           '06':'Шестое',
#           '07':'Седьмое',
#           '08':'Восьмое',
#           '09':'Девятое',
#           '10':'Десятое',
#           '11':'Одинадцатое',
#           '12':'Двенадцатое',
#           '13':'Тринадцатое',
#           '14':'Четырнадцатое',
#           '15':'Пятнадцатое',
#           '16':'Шестнадцатое',
#           '17':'Семнадцатое',
#           '18':'Восемнадцатое',
#           '19':'Девятнадцатое',
#           '20':'Двадцатое',
#           '21':'Двадцать первое',
#           '22':'Двадцать второе',
#           '23':'Двадцать третье',
#           '24':'Двадцать четвертое',
#           '25':'Двадцать пятое',
#           '26':'Двадцать шестое',
#           '27':'Двадцать седьмое',
#           '28':'Двадцать восьмое',
#           '29':'Двадцать девятое',
#           '30':'Тридцатое',
#           '31':'Тридцать первое'
#           }
# dict_month={'01':'Январь',
#             '02':'Ферваль',
#             '03':'Март',
#             '04':'Апрель',
#             '05':'Май',
#             '06':'Июнь',
#             '07':'Июль',
#             '08':'Август',
#             '09':'Сентябрь',
#             '10':'Октябрь',
#             '11':'Ноябрь',
#             '12':'Декабрь'
#             }
# data_list=data.split('.')
# print(data_list)
# for key in dict_day:
#     if data_list[0] == key:
#         data_list[0] = dict_day[key]
# for key in dict_month:
#     if data_list[1]==key:
#         data_list[1] = dict_month[key]
# answer_data = data_list[0] + ' ' + data_list[1] + ' ' + data_list[2] + ' ' "года"
# print(answer_data)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


# import random
# n=10
# a=[]
# for i in range(0,n):
#     random.randint(-100,100)
#     a.append(random.randint(-100,100))
# print(a)



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


# a=[1,2,3,4,5,6,7,8,8,7,6,]
# b=set(a)
# print(list(b))


# a=[1,2,3,4,5,6,7,8,8,7,6,]
# b=[]
# for item in a:
#     if a.count(item)==1:
#         b.append(item)
# print(b)



# HARD
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3



# a=[]
# for i in range(0,20):
#     a.append(i+1)
# print(i)




# fruit=['яблоко','банан','груша','слива','апельсин','персик','киви']
# x=1
# for i in fruit:
#     print(x,'.' "{:>15}".format(i))
#     x+=1


# print(17*'*')
# print('*'+15*' '+'*')
# print('*'+15*' '+'*')
# print(17*'*')

# a = int(input())
# b = int(input())
# print('Квадрат суммы', a, 'и', b, 'равен',((a+b)**2))
# print('Сумма квадратов', a, 'и', b, 'равна', ((a**2)+(b**2)))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(a**b+c**d)

# n = str(input())
# print(int(int(n)+int((str(n)+str(n)))+int((str(n)+str(n)+str(n)))

# a = len(input())
# b = len(input())
# c = len(input())
#
# if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
#     print('YES')
# else:
#     print('NO')


# string = input()
# count = int(input())
# for i in range(count):
#     print(string)

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')


# n = int(input())
# for i in range(n, 0, -1):
#     print(i*'*')


# for i in range(5, 0, -1):
#     print(i, end=' ')
# print('Взлетаем!!!')


# m = int(input())
# n = int(input())
# for _ in range(n, m, -2):
#     if _%17==0 or (_%5 and _%3) or _%10==9:
#     print(_)



# n = int(input())
# for _ in range(1, 10):
#     print(n, 'x', _, '=', _*n)


# a = int(input())
# b = int(input())
# counter =0
# for i in range(a, b+1):
#       if i**3%10==4 or i**3%10==9:
#         counter +=1
# print(counter)





# n = int(input())
# total =0
# for i in range(n):
#       n = int(input())
#       total+=n
# print(total)



# for i in range(10):
#     n = int(input())
#     if n!=0:
#         n *=n
# print(i)

#
# n = int(input())
# total=0
# for i in range(1,n+1):
#     if n%i==0:
#         total+=i
# print(total)

# fib1 = fib2 = 1
# n = int(input())
# print(fib1, fib2, end=' ')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')


    # num= 12345
    # max=0
    # min=9
    # while num != 0:
    #     last_digit = num % 10
    #     if last_digit>max:
    #         max=last_digit
    #     if last_digit<min:
    #         min=last_digit
    #     num = num // 10
    # print('Максимальная цифра равна', max)
    # print('Минимальная цифра равна', min)


# n = int(input())
# last_digit = n%10
# summa = 0
# proizvedenie = 1
# count = 0
# while n != 0:
#     l_d=n%10
#     print(l_d)
#     summa+=l_d
#     proizvedenie*=l_d
#     count+=1
#     f_d = n
#     n = n//10
# print('сумма', summa)
# print('количество цифр', count)
# print('Произведение', proizvedenie)
# print('среднее арифметическое его цифр', summa/count)
# print('его первую цифру', f_d)
# print('сумму его первой и последней цифры', f_d+last_digit)



# a = int(input())
# ld = a%10
# flag = True
# while a!=0:
#     if ld!=a%10:
#         flag= False
#     a = a // 10
# if flag==False:
#     print('NO')
# else:
#     print('YES')

# a = int(input())
# flag = True
# while a != 0:
#     ld = a % 10
#     pld = ((a // 10) % 10)
#     if ld>pld :
#         flag = False
#     a = a // 10
# if flag == False:
#     print('NO')
# elif flag == True:
#     print('YES')




# n=int(input())
# # for i in range(1,n+1):
# #     if 5<=i<=9 or 17<=i<=37 or 78<=i<=87:
# #         i+=1
# #         continue
# #     print(i)


# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x > 0:
#         p = p * x
#         count += 1
# if count > 0:
#     print(x)
#     print(p)
# else:
#     print('NO')




# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)


# n = int(input())
# while n>0:
#     if n//10 ==0:
#         break
#     n =n//10
# print(n)


# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)


# from time import *
# for hour in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hour,minutes, seconds, sep=':', end='')
#             sleep(1)
#             print(end='\r')


# n = int(input())
# for i in range(1, n+1):
#     for j in range(1,10):
#         print(i, '+', j, '=', i+j)
#     print()


# n = int(input())
# for i in range(1,int((n/2)+2)):
#     for j in range(i):
#         print('*', end = '')
#     print()
# for i in range(int((n/2)), 0, -1):
#     for j in range(i):
#         print('*', end = '')
#     print()


# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(i, end='')
#     print()

# for n in range(10):
#     for k in range(10):
#         for m in range(10):
#             if 28*n+30*k+31*m==365:
#                 print('n=', n, 'k=', k, 'm=', m, end='')
#     print()



# total = float(100)
# for bykov in range(1,11):
#     for kow in range(1,21):
#         for tel in range(1,201):
#             if bykov*10+kow*5+tel*0.5==100:
#                 if bykov+kow+tel==100:
#                     print(bykov,kow,tel)
# print()

# for a in range(25,28):
#     for b in range(82, 85):
#         for c in range(100,111):
#             for d in range(120,134):
#                 for e in range(140,150):
#                     print(a, b, c, d, e)
#                     if a**5+b**5+c**5+d**5==e**5:
#                         print(a+b+c+d+e)
#                         break
#
#
# a=27
# b=84
# c=110
# d=133
# e=144
#
# print((a**5+b**5+c**5+d**5))
# print(e**5)




# n = int(input())
# num = 1
# cnt = 1
# for i in range(n):
#     for j in range(cnt):
#         print(num, end = ' ')
#         num += 1
#     print()
#     cnt += 1


# n = int(input())
# for i in range(1,n):
#     for j in range(1,i):
#         print(j, end = ' ')
#     print()

# n = int(input())
# for i in range(1, n+1):
#     for j in range(i):
#         print(j+1, end = '')
#     print()



# n = int(input())
# for i in range(1, n+1):
#     for j in range(i):
#         print(j+1, end = '')
#     for k in range(i-1, 0, -1):
#         print(k, end = '')
#     print()


# a= int(input())
# b= int(input())
# sum_max=0
# count = 0
# for i in range(a,b+1):
#     sum=0
#     for j in range(1, b+1):
#         if i%j==0:
#             sum+=j
#             if sum >=sum_max:
#                 sum_max=sum
#                 count = j
# print(count, sum_max)


# n = int(input())
# count=0
# for i in range(1,n+1):
#     count_d=0
#     for j in range(1, n+1):
#         if i%j==0:
#             count_d+=1
#             if count<j:
#                 count=j
#     print(count, count_d*'+')




# n= int(input())
# while n>9:
#     sum = 0
#     while n>0:
#         last_digit=n%10
#         sum+=last_digit
#         n=n//10
#     n=sum
# print(n)


# n=int(input())
# while n >9:
#     n-=9
# print(n)


# from math import factorial
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum+=factorial(i)
# print(sum)


# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     count=0
#     for j in range(2, i):
#         if i%j==0:
#             count+=1
#     if count==0 and i!=1:
#         print(i)


# n = int(input())
# res = 1
# i = 2
# while i <= n:
#     res *= i
#     i += 1
# print(res)

# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)



# n = int(input())
# counter = 0
# while n> 0:
#     n//=10
#     counter += 1
# print(counter)




# n = int(input())
# s = 0
# while n >0:
#     if (n % 10)%2 == 0:
#         s += n % 10
#     n //= 10
# print(s)




# count = 0
# maximum = -10**6
# for i in range(8):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')




# count = 0
# maximum = -10**6
# for i in range(4):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count == 0:
#     print('NO')
# else:
#     print(count)
#     print(maximum)




# n = int(input())
# print(19*'*',sep='  ')
# for i in range(n-2):
#     print('*', 17*' ', '*',sep='')
# print(19*'*')
#
# *******************
# *                 *
# *                 *
# *                 *
# *******************
#
# *******************
# *                 *
# *                 *
# *                 *
# *******************

# n= int(input())
# while n>0:
#     if 100<=n<=999:
#         n =n%10
#         break
#     else:
#         n=n//10
# print(n)






# n= int(input())
# count_3 = 0
# last_digit=n%10
# count_last=0
# count_chet=0
# summ5=0
# proizv7=1
# count0_5=0
# while n>0:
#     if n%10==3:
#         count_3+=1
#     if last_digit==n%10:
#         count_last+=1
#     if n%10%2==0:
#         count_chet+=1
#     if n%10>5:
#         summ5+=n%10
#     if n%10>7:
#         proizv7*=n%10
#     if n%10==0 or n%10==5:
#         count0_5+=1
#     n=n//10
# print(count_3, count_last, count_chet, summ5, proizv7, count0_5, sep='\n')




# count = 0
# for a in range(33):
#     for b in range(33):
#         for c in range(33):
#             for d in range(33):
#                 if a != b and a != c and a != d and b != c and b != d and c != d and a<b and c<d:
#                     if a**3+b**3==c**3+d**3:
#                         count +=1
#                         print(count, a, b, c, d)
#                         print(a**3+b**3, '=', c**3+d**3)



# s = input()
# for c in range(-1, -len(s)-1, -1):
#     print(s[c])


# s_i = input()
# s_f = input()
# s_o = input()
# print(s_f[0]+s_i[0]+s_o[0])

# s = input()
# sum = 0
# for c in range(len(s)):
#     sum+=int(s[c])
# print(sum)


# s = input()
# for i in range(10):
#     if i in s:
#         print(i)


# s = input()
# count_plus = 0
# count_star = 0
# for c in range(len(s)):
#     if s[c]=='+':
#         count_plus+=1
#     if s[c]=='*':
#         count_star+=1
# print('Символ + встречается', count_plus, 'раз', '\n' 'Символ * встречается', count_star, 'раз')



# s = input()
# soglas = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
# glas = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
# count_gl = 0
# count_sogl = 0
# for c in range(len(s)):
#     if s[c] in glas:
#         count_gl +=1
#     elif s[c] in soglas:
#         count_sogl +=1
# print('Количество гласных букв равно', count_gl)
# print('Количество согласных букв равно', count_sogl)


# x = int(input())
# n = ''
# while x > 0:
#     y = str(x % 2)
#     n = y + n
#     x = int(x / 2)
# print(n)

# x = int(input())
# print (bin(x))

# s = 'abcdefghij'
# s[:-1]
# print(s[::-1])


# s = input()
# for c in range(len(s)):
#     for ch in range(-1,-len(s)-1,-1):
#         if s[c] == s[ch]:
#             print(s[c], '=', s[ch])



# s = input()
# for c in range(len(s)):
#     for ch in range(-1,-len(s)-1,-1):
#         if s[c] == s[ch]:
#             print(s[c], '=', s[ch])




# s = input()
# s_u = s[::-1]
# count=0
# for c in range(len(s)):
#     if s[c] == s_u[c]:
#         count+=1
# if count==len(s):
#     print('YES')
# else:
#     print('NO')



# s ='123456789'
# for c in range(-1,-len(s)-1,-1):
#     print(s[c])



# s = input()
# print(len(s))
# print(3*s)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1:])


# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])


# s = input()
# if int(len(s)%2) == 1:
#     print(s[int(len(s)/2+1)::]+s[:int(len(s)/2+1):])
# else:
#     print(s[int(len(s)/2)::]+s[:int(len(s)/2):])


# s =  str.lower(input())
# if 'хорош' in s:
#     print('YES')
# else:
#     print('NO')

# s = input()
# count = 0
# for c in range(len(s)):
#     if s[c] in 'abcdefghijklmnopqrstuvwxyz':
#         count+=1
# print(count)



# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))

# s = 'www.stepik.org'
# print(s.startswith('www'))

# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))


# s =  str.lower(input())
# print(s)
# print('Аденин:', ' ',s.count('а'))
# print('Гуанин:', ' ',s.count('г'))
# print('Цитозин:', ' ',s.count('ц'))
# print('Тимин:', ' ',s.count('т'))


# n = int(input())
# count=0
# while n!=0:
#     s = input()
#     if s.count('11')>=3:
#         count+=1
#     n-=1
# print(count)

# s = input()
# count = 0
# for c in range(len(s)):
#     if s[c] in '1234567890':
#         count+=1
# print(count)

# s = input()
# if s.endswith('.com') or s.endswith('.ru') == True
#     print('YES')
# else:
#     print('NO')


# s = input()
# count = 0
# b =''
# for c in range(len(s)):
#     if s.count(s[c]) >= count:
#         count = s.count(s[c])
#         b=s[c]
# print(b)



# s = input()
# if s.count('f')>=2:
#     print(s.find('f'), s.rfind('f'))
# elif s.count('f')==1:
#     print(s.find('f'))
# elif s.count('f') == 0:
#     print('NO')



# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')
# print('In 2010, someone paid 10K Bitcoin for two pizzas.')



# a = int(input())
# b = int(input())
# for c in range(a, b+1):
#     print(chr(c), end=' ')


# s = input()
# for c in range(len(s)):
#     print(ord(s[c]), end=' ')

# n = int(input())
# s = input()
# for c in range(len(s)):
#     if ord(s[c])-n < 97:
#         print(chr(ord(s[c])-n+26), end='')
#     else:
#         print(chr(ord(s[c])-n), end='')

# s = input()
# for c in range(len(s)):
#     if c==0 or c%3==0:
#         continue
#     else:
#         print(s[c], end='')



# s = input()
# if s.count('f')==0:
#     print(int('-2'))
# elif s.count('f')==1:
#     print(int('-1'))
# elif s.count('f')>=2:
#     s = s.replace('f', '1', 1)
#     print(s.find('f'))


s = input()
s.find('h')
s.rfind('h')
s1 = s[:s.find('h')+1]
s2 = s[s.rfind('h'):]
s3 = s[s.find('h')+1:s.rfind('h'):]
print(s1+s3[::-1]+s2)