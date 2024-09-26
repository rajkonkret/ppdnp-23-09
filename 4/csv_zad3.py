import pandas

# pip install pandas

data = pandas.read_csv('records_3_discount.csv', delimiter=";")

print(data)
#    sku  exp_date  price
# 0    1     today    200
# 1    2     today     50
# 2    3  tomorrow    100
# 3    4     today    700

print(data.columns)  # Index(['sku', 'exp_date', 'price'], dtype='object')
print(data.values)
# [[1 'today' 200]
#  [2 'today' 50]
#  [3 'tomorrow' 100]
#  [4 'today' 700]]
print(data.items)
# <bound method DataFrame.items of    sku  exp_date  price
# 0    1     today    200
# 1    2     today     50
# 2    3  tomorrow    100
# 3    4     today    700>
