print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")
tip_percent = input("How much tip would you like to give? 10, 12, or 15? ")
num_tippers = input("How many people to split the bill? ")

bill_as_float = float(bill)
tip_percent_as_int = int(tip_percent)
num_tippers_as_int = int(num_tippers)

tip_add_percent = tip_percent_as_int / 100 + 1
bill_per_person_with_tip = bill_as_float / num_tippers_as_int * tip_add_percent
final_amount = "{:.2f}".format(bill_per_person_with_tip)

print(f"Each person should pay: ${final_amount}")
