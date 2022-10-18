maney = int(input('Введите сумму вклада: '))
print ("maney =", maney)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
rate_1 = (per_cent['ТКБ'])
rate_2 = (per_cent['СКБ'])
rate_3 = (per_cent['ВТБ'])
rate_4 = (per_cent['СБЕР'])
deposit = [int((maney*rate_1)/100), int((maney*rate_2)/100), int((maney*rate_3)/100), int((maney*rate_4)/100)]
print ("deposit =", deposit)
print ("Максимальная сумма, которую вы можете заработать —", max(deposit))