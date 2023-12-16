# CUONG VO - 131116

# Import library for path create, url open and csv writeer
import os
from urllib.request import urlopen
import csv

print(f'Download the data ....')
# Create for the stock list
stock_list = ['GOOG', 'IBM', 'MSFT', 'PFE', 'TSLA', 'F', 'AMD', 'UBER']

# Download csv file from yahoo finance for each stock code in stock list and restore it into folder stoct_list
for stock in stock_list:
    url = """https://query1.finance.yahoo.com/v7/finance/download/"""+ stock \
            +"""?period1=1671165576&period2=1702701576"""\
            +"""&interval=1d&events=history&includeAdjustedClose=true"""
    local_path = os.path.join('stock_list', stock + '.csv')
    with urlopen(url) as image, open(local_path, 'wb') as f:
        f.write(image.read())

# Create path for reading and writign the data
working_path = os.getcwd()
working_path = os.path.join(working_path, 'stock_list')
writing_path = os.getcwd()
writing_path = os.path.join(writing_path, 'price_analyze')

# Create a list to replace the dataframe to record the price. 
for stock in stock_list:
    # Create path to capture csv file and load the file
    file_path = os.path.join(working_path, stock + '.csv')
    with open(file_path, 'r') as f:
        stock_price = f.readlines()
    # Record price into the list
    price_table = []
    for price in stock_price:
        tmp = price.replace('\n', '').split(sep=',')
        price_table.append(tmp)
    # Create new column 'Change' and calculate the change price for each stock code
    price_table[0].append('Change')
    for i in range(1, len(price_table)):
        open_price = float(price_table[i][1])
        close_prince = float(price_table[i][4])
        change_price = str((close_prince - open_price) / open_price)
        price_table[i].append(change_price)
    # using csv library to write the file    
    file_path = os.path.join(writing_path, stock + '.csv')
    with open(file_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(price_table)

print(f'Download the data completed')
# Create programs to search for the file with stock code 
index = 'Y'
while index == 'Y':    
    print(f'Please input the stock code for searching: ', end = '')
    stock_name = input()
    if os.path.exists(os.path.join(working_path, stock_name + '.csv')):
        print(f'Source data of {stock_name} stock: {os.path.join(working_path, stock_name + ".csv")}')
        print(f'Analyze data of {stock_name} stock: {os.path.join(writing_path, stock_name + ".csv")}')
    else: print(f'File not found')
    print(f'Continue ? [Y/N]: ', end ='')
    tmp = input()
    if tmp == 'N': index = 'N'








