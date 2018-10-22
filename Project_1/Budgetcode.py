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


def timeseries(df):  # time series chart

    sums = sumkeys(makedatedict(df))
    unique_date_list = list(date_dict.keys())
    ttsum = np.cumsum(sums)
    plt.scatter(unique_date_list, ttsum, color = "red")
    numx = np.arange(0, len(unique_date_list))
    plt.plot(np.unique(numx), np.poly1d(np.polyfit(numx, ttsum, 1))(np.unique(numx)))
    plt.ylabel('Total $ Spent')
    plt.xlabel('Date')
    
    plt.show()

def pie(df): # pie chart 

    sums = sumkeys(makecategorydict(df))
    sizes = []
    unique_category_list = list(category_dict.keys())
    total_values = sumitems(df)
    for items in sums:
        pp = items/total_values
        sizes.append(pp)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=unique_category_list, autopct='%1.1f%%',textprops={'fontsize': 14})
    ax1.axis('equal')
    ax1.set_title('Pie Chart Based on Type') 
    plt.show()



def makedatedict(df):  # making the date dictionary

    list_of_prices = df["Ammount"].tolist()
    list_of_dates = df["Date"].tolist()

    date_strings = [str(i) for i in list_of_dates]
    for index in range(len(date_strings)):
        if date_strings[index] in date_dict:
            (date_dict[date_strings[index]]).append(convertprice(list_of_prices[index]))
        else:
            date_dict[date_strings[index]] = [convertprice(list_of_prices[index])]
    return date_dict


def makecategorydict(df):  # making the type dictionary

    list_of_prices = df["Ammount"].tolist()
    list_of_categories = df["type"].tolist()

    for index in range(len(list_of_categories)):
        lowercaseItem = str(list_of_categories[index]).lower()
      
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
