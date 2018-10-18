import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('budget.csv')

x = df.describe()
y = df["Date"]

price = None
category = None
date = None

date_dict = {}
list_of_dates = df["Date"].tolist()
list_of_prices = df["Ammount"].tolist()


# Lets the user modify the date, category, or amount given a row in a dataframe
def modifyEntry(df, row, date=None, category=None, amount=None):


    # Verify if date was provided
    if date != None:
        try:
            df.at[row, "Date"] = pd.to_datetime(date, errors='raise').date()  # The format is normalized to M/D/Y
        except:
            print("Please enter date in M/D/Y ex. 10/2/2018")
            raise ValueError

    # Verify if category was provided
    if category != None:
        try:
            category = str(category)
            if not category.isalpha():  # Check to make sure string contains only letters
                raise TypeError
            df.at[row, "type"] = category
        except TypeError:
            print('Please enter a string for the type')
            raise TypeError

    # Verify if amount was provided
    if amount != None:
        amount = str(amount)

        try:
            amount = format(float(amount), '.2f')  # Format the string to have 2 decimal points

            if float(amount) >= 0:  # Make sure not negative number
                dollarAmount = '$' + amount  # Add dollar sign to the string
                df.at[row, "Ammount"] = dollarAmount
            else:
                raise ValueError
        except ValueError:
            print('Please enter a float for the amount')
            raise ValueError

    return df
    # f = open("budget.csv", "w")
    # df.to_csv(f, index=False, header=True)

# Deletes an entire row in a dataframe and reindexes the dataframe
def deleteRowEntry(df, row):
    df = df.drop([row]).reset_index(drop=True)
    return df

# Amount, Category, and Date are optional params for debugging
# Typically these would be entered by the user via the keyboard
def newExpense(df, amount=None, category=None, date=None):

    # If all optional params are None, then read input
    if not amount and not category and not date:
        amount = input("Enter Amount")
        category = input("Enter Category")
        date = input("Enter Date")

    rowIndex = df.shape[0] # get the row index to add to
    df = modifyEntry(df, rowIndex, date=date, category=category, amount=amount)
    
    return df


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
    plt.xlabel('Date')
    plt.show()
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

    modifyEntry(df, row = 0, amount = 10000)

    newExpense(df)

    timeseries()
    print(df)


    # y = newexpense()
    # x = sumitems(y)
    # print("Sum:", x)




main()
