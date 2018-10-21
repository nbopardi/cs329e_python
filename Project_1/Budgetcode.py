import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def readInCSV(title):
    df = pd.read_csv(title)
    return convertToDateTime(df)

def convertToDateTime(df):
    rows = df.shape[0] # The number of rows in the dataframe
    for i in range(0,rows): # Change all dates to pandas date time objects for sorting later on
        df.at[i, "Date"] = pd.to_datetime(df.at[i,"Date"], errors='raise').date()

    return df

df = readInCSV('budget.csv')

price = None
category = None
date = None

date_dict = {}
category_dict = {}

list_of_dates = df["Date"].tolist()
list_of_prices = df["Ammount"].tolist()
list_of_categories = df["type"].tolist()



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

    #f = open("budget.csv", "w")
   # df.to_csv(f, index=False, header=True)
    date_dict.clear()
    category_dict.clear()
    return df

# Deletes an entire row in a dataframe and reindexes the dataframe
def deleteRowEntry(df, row):
    df = df.drop([row]).reset_index(drop=True)
    date_dict.clear()
    category_dict.clear()
    return df


def newexpense(df, amount=None, category=None, date=None):
    # If all optional params are None, then read input
    if not amount and not category and not date:
        amount = input("Enter Amount")
        category = input("Enter Category")
        date = input("Enter Date")

    rowIndex = df.shape[0]  # get the row index to add to
    df = modifyEntry(df, rowIndex, date=date, category=category, amount=amount)
    date_dict.clear()
    category_dict.clear()
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

    sums = sumkeys(makedatedict())
    unique_date_list = list(date_dict.keys())
    ttsum = np.cumsum(sums)
    plt.scatter(unique_date_list, ttsum, color = "red")
    numx = np.arange(0, len(unique_date_list))
    plt.plot(np.unique(numx), np.poly1d(np.polyfit(numx, ttsum, 1))(np.unique(numx)))
    plt.ylabel('Total $ Spent')
    plt.xlabel('Date')
    plt.show()
    return ttsum

def pie():

    sums = sumkeys(makecategorydict())
    sizes = []
    unique_category_list = list(category_dict.keys())
    total_values = sumitems(df)
    for items in sums:
        pp = items/total_values
        sizes.append(pp)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=unique_category_list, autopct='%1.1f%%')
    plt.show()



def makedatedict():  # making the dictionary

    list_of_prices = df["Ammount"].tolist()
    list_of_dates = df["Date"].tolist()

    for index in range(len(list_of_dates)):
        if list_of_dates[index] in date_dict:
            (date_dict[list_of_dates[index]]).append(convertprice(list_of_prices[index]))
        else:
            date_dict[list_of_dates[index]] = [convertprice(list_of_prices[index])]
    return date_dict


def makecategorydict():  # making the dictionary

    list_of_prices = df["Ammount"].tolist()
    list_of_categories = df["type"].tolist()

    for index in range(len(list_of_categories)):
        lowercaseItem = str(list_of_categories[index]).lower()
        print(lowercaseItem)
        if lowercaseItem in category_dict:
            (category_dict[list_of_categories[index]]).append(convertprice(list_of_prices[index]))
        else:
            category_dict[list_of_categories[index]] = [convertprice(list_of_prices[index])]
    return category_dict


def sumkeys(dick):  # summing the values in each key
    list_of_date_sums = []
    for items in dick:
        x = sum(dick[items])
        list_of_date_sums.append(x)

    return list_of_date_sums
    # print("Total Spent on Each Date:", listOfDateSums)


def main():
    global df

    # df = modifyEntry(df, row = 0, amount = 10000)

    print(df)
    modifyEntry(df, 0, None, None, 10)
    modifyEntry(df, 1, None, "school", None)
    print("\n", df)
    timeseries()
    pie()
    # method_to_execute = input("What method will you run: \n 0 - new expense \n 1 - modify entry\n 2 - delete row \n 3 - graph \n 4 - exit\n\t")

    # while float(method_to_execute) != 3:
    #     if float(method_to_execute) == 0:
    #         entry_details = input("input Price, Category, Date (with spaces between):\t")
    #         entry_details_list = entry_details.split()
    #         newexpense(entry_details_list[0], entry_details_list[1], entry_details_list[2])
    #
    #     elif float(method_to_execute) == 1:
    #         df_row_index = input("which row will be CHANGED:\t")
    #         entry_details_date = input("input Date:\t")
    #         entry_details_type = input("input Type:\t")
    #         entry_details_cost = input("input Cost:\t")
    #         modifyEntry(df, df_row_index, entry_details_date, entry_details_type, entry_details_cost)
    #
    #     elif float(method_to_execute) == 2:
    #         df_row_index = input("which row will be DELETED:\t")
    #         deleteRowEntry(df, df_row_index)
    #
    #     elif float(method_to_execute) == 3:
    #         timeseries()
    #
    #     method_to_execute = input("What method will you run: \n 0 - new expense \n 1 - modify entry\n 3 - delete row \n 4 - exit")



    # y = newexpense()
    # x = sumitems(y)
    # print("Sum:", x)




# main()
