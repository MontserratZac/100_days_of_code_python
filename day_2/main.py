#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_as_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))

bill_per_person = round(((tip_as_percent + 1) *total_bill) / (people), 2)
#Para que nuestra cifra tenga un formato con dos decimales 
bill_per_person_format = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person_format}")