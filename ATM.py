# Simulate bank transaction
balance = 500
# Get user input for withdrawal amount
withdrawal_amount = float(input("Enter the amount to withdraw: "))

# Check if the withdrawal amount is valid and if there are sufficient funds
if withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than R0")

    # check if the withdrawal amount is less than or equal to the balance
elif withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print(f"Withdrawal successful! Remaining balance: R{balance}")
else:
    print("Declined. Insufficient funds.")
    input("Press Enter to exit.")
    
