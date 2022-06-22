print("welcome to the tip calculator")
t_bill=input("enter the total bill")
p_tip=int(input("what percentage tip would you like to give"))
total_bill=float(p_tip)/100*float(t_bill) + float(t_bill)
n=int(input("enter the number of people"))
final=total_bill/n
round(final, 2)
print(f"the total amount to be paid by each individual is: {final}")