from helpers.get_info import get_my_tx

res = get_my_tx('markgagnon', 'root')
for el in res:
  print('Done')
  print(el)