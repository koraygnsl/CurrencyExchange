import requests
import json
import time

url = str.__add__('http://data.fixer.io/api/latest?access_key=' , 'bb6305df2a03b8324435545dbb897193')
data = requests.get(url).json()
rates = data["rates"]

class Currency_convertor:

	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()

		
		self.rates = data["rates"]

	
	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		
		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

print("*******CALCULATIONS ARE BASED ON EURO*******")
print("********************************************")
time.sleep(2)

choise = 1
while choise != 3:
    print("******* WELCOME TO CURRENCY EXCHANGE *******")
    print("********************************************")
    print("1. SEE RATES \n2. EXCHANGE \n3. EXIT")
    choise = int(input("ENTER YOUR CHOISE : "))
    if choise == 2:
        c = Currency_convertor(url)
        from_country = input("FROM COUNTRY : ")
        to_country = input("TO COUNTRY : ")
        from_country = from_country.upper()
        to_country = to_country.upper()
        amount = int(input("AMOUNT : "))

        while to_country not in rates or from_country not in rates:
            print("INVALID COUNTRY... PLEASE TRY AGAIN")
            time.sleep(1)
            from_country = input("FROM COUNTRY : ")
            to_country = input("TO COUNTRY : ")
            from_country = from_country.upper()
            to_country = to_country.upper()
            amount = int(input("AMOUNT : "))
        
        c.convert(from_country,to_country,amount)
        time.sleep(3)
    
    elif choise == 1:
        for rate,value in rates.items():           
            print(rate + " : " + str(value))
            time.sleep(0.04)
        time.sleep(3)
    
    else:
        break