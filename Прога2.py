a = int(input('Введите сумму вклада: '))
print ("maney =", a)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
b = 100
print ("deposit =", [(int((a*per_cent['ТКБ'])/b)), (int((a*per_cent['СКБ'])/b)), (int((a*per_cent['ВТБ'])/b)), (int((a*per_cent['СБЕР'])/b))])
list = [(a*per_cent['ТКБ'])/b, (a*per_cent['СКБ'])/b, (a*per_cent['ВТБ'])/b, (a*per_cent['СБЕР'])/b]
w = 'deposit[i]' 
w = int(max(list))
print ("Максимальная сумма, которую вы можете заработать —", w)