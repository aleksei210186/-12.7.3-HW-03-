maney = int(input('Введите сумму вклада: '))
print ("maney =", maney)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [int((maney*per_cent['ТКБ'])/100), int((maney*per_cent['СКБ'])/100), int((maney*per_cent['ВТБ'])/100), int((maney*per_cent['СБЕР'])/100)]
print ("deposit =", deposit)
print ("Максимальная сумма, которую вы можете заработать —", max(deposit))