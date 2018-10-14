# Read in csv

import pandas as pd

df = pd.read_csv('budget.csv')

# Lets the user modify the date, category, or amount given a row in a dataframe
def modifyEntry(df, row, date=None, category=None, amount=None):
	
	# Verify if date was provided
	if date != None:
		try:
			df.at[row, "Date"] = pd.to_datetime(date, errors = 'raise').date() # The format is normalized to M/D/Y
		except:
			print("Please enter date in M/D/Y ex. 10/2/2018")
			raise ValueError

	# Verify if category was provided
	if category != None:
		try:
			category = str(category) 
			if not category.isalpha(): # Check to make sure string contains only letters
				raise TypeError
			df.at[row, "type"] = category
		except TypeError:
			print('Please enter a string for the type')
			raise TypeError

	# Verify if amount was provided		
	if amount != None:
		amount = str(amount)

		try:
			amount = format(float(amount), '.2f') # Format the string to have 2 decimal points
			
			if float(amount) >= 0: # Make sure not negative number
				dollarAmount = '$' + amount # Add dollar sign to the string
				df.at[row, "Ammount"] = dollarAmount
			else:
				raise ValueError
		except ValueError:
			print('Please enter a float for the amount')
			raise ValueError
		

# Deletes an entire row in a dataframe and reindexes the dataframe
def deleteRowEntry(df, row):
	df = df.drop([row]).reset_index(drop = True)
	return df

