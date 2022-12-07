#savings.py
#HMWK_3



initial_balance = float(input("Enter the initial balance: "))
interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
final_balance = float(input("Enter the final balance desired: "))


print(f"Initial balance: {round(initial_balance, 2)}")


balance = initial_balance


num_years = 0


while balance < final_balance:
    
    balance = balance * (1 + interest_rate)
    num_years += 1

    
    print(f"After {num_years} year(s), the balance is {round(balance, 2)}")


print(f"Final balance: {round(balance, 2)}")
