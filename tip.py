bill = int(input("What is your total bill amount?"))
tip = int(input("What is your tip percentage?"))
def total_calc(bill,tip):
    total = bill*(1+0.01*tip)
    total = round(total,2)
    print(f"Please pay ${total}")
total_calc(bill,tip)