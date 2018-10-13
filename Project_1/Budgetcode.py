import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('budget.csv')

print(df)

x = df.describe()
y = df["Date"]

price = None
category = None
date = None

date_dict = {}
list_of_dates = df["Date"].tolist()
list_of_prices = df["Ammount"].tolist()


def newexpense():
    global price
    global category
    global date
    global df
    price = input("Enter Price")
    category = input("Enter Type of Expense")
    date = input("Enter Date")

    f = open("budget.csv", "a")
    f.write('\n')

    df2 = pd.DataFrame(columns=['Date', 'type', 'Ammount'])
    df2.loc[0] = [date, category, price]
    df2.to_csv(f, index=False, header=False)

    f.close
    df3 = pd.read_csv('budget.csv')

    return df3


def convertprice(price):
    length = len(price)
    sObject = slice(1, length)
    numerical = float(price[sObject])
    return numerical


def sumitems(df):
    z = df["Ammount"]
    total = 0.0 
    for items in z:
        length = len(items)
        sObject = slice(1, length)
        numerical = items[sObject]
        total += float(numerical)
    
    return total


def timeseries():

    sums1 = datesums(combiningdates())
    unique_date_list = date_dict.keys()
    plt.plot(unique_date_list, np.cumsum(sums1))
    plt.ylabel('Total $ Spent')


def combiningdates():

    for index in range(len(list_of_dates)):
        if list_of_dates[index] in date_dict:
            (date_dict[list_of_dates[index]]).append(convertprice(list_of_prices[index]))
        else:
            date_dict[list_of_dates[index]] = [convertprice(list_of_prices[index])]
    return date_dict


def datesums(dick):
    list_of_date_sums = []
    for items in dick:
        x = sum(dick[items])
        list_of_date_sums.append(x)

    return list_of_date_sums
    # print("Total Spent on Each Date:", listOfDateSums)


def main():
    global df
    timeseries()

    # y = newexpense()
    # x = sumitems(y)
    # print("Sum:", x)

    plt.show()


main()
