#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill?"))

percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

divide_people = int(input("How many people to split the bill?"))

percentage_new = ((percentage / 100) * total_bill) + total_bill
divide_people_new = percentage_new / divide_people
print(f"Each person should pay: ${divide_people_new:.2f}")