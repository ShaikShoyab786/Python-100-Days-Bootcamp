print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage % tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip_amount = tip_percent * bill
total_bill = total_tip_amount + bill
bill_per_each_person = total_bill / people
final_bill_per_person = round(bill_per_each_person, 2)

print(f"Each person Should pay $ {final_bill_per_person} ")