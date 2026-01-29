print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip/100)
bill_with_tip = bill + tip_amount
split_bill = bill_with_tip/people
final_bill_per_person = round(split_bill, 2)
print(f"Each person should pay ${final_bill_per_person}")
