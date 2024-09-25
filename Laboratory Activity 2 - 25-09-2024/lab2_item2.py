def calculate_discount(total_amount):
    if total_amount > 5000:
        discount = total_amount * 0.10  
    else:
        discount = total_amount * 0.05  
    
    final_price = total_amount - discount
    return discount, final_price

while True:
    
    total_amount = float(input("Enter the total purchase amount: "))

    discount, final_price = calculate_discount(total_amount)

    print(f"Initial Purchase Amount: {total_amount:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Price: {final_price:.2f}")

    try_again = input("Do you want to try again? (yes/no): ").lower()    
    
    if try_again != 'yes':
        print("Thank you!")
        break
