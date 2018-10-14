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


def convertprice(price):  # removes dollar sign
    length = len(price)
    sObject = slice(1, length)
    numerical = float(price[sObject])
    return numerical


def sumitems(df):  # sums the items
    z = df["Ammount"]
    total = 0.0 
    for items in z:
        length = len(items)
        sObject = slice(1, length)
        numerical = items[sObject]
        total += float(numerical)
    
    return total


def timeseries():  # time series chart

    sums1 = sumkeys(makedict())
    unique_date_list = list(date_dict.keys())
    ttsum = np.cumsum(sums1)
    plt.scatter(unique_date_list, ttsum, color = "red")
    numx = np.arange(0,len(unique_date_list))
    plt.plot(np.unique(numx), np.poly1d(np.polyfit(numx, ttsum, 1))(np.unique(numx)))
    plt.ylabel('Total $ Spent')
    return ttsum


def makedict():  # making the dictionary

    for index in range(len(list_of_dates)):
        if list_of_dates[index] in date_dict:
            (date_dict[list_of_dates[index]]).append(convertprice(list_of_prices[index]))
        else:
            date_dict[list_of_dates[index]] = [convertprice(list_of_prices[index])]
    return date_dict


def sumkeys(dick):  # summing the values in each key
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
