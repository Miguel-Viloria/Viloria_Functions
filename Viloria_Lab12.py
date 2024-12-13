# Function Code for menu food items
def leche_flan():
    return "Leche Flan", 120

def fruit_salad():
    return "Fruit Salad", 100

def mango_graham():
    return "Mango Graham", 150

def cordon_bleu():
    return "Cordon Bleu", 200

def menudo():
    return "Menudo", 130

def macaroni_salad():
    return "Macaroni Salad", 125

def carbonara():
    return "Carbonara", 135

def christmas_package():
    return "Christmas Handaan Package", 1000

# Display Menu Function Code
def display_menu():
    print("Menu:")
    print("1. Leche Flan - 120 pesos")
    print("2. Fruit Salad - 100 pesos")
    print("3. Mango Graham - 150 pesos")
    print("4. Cordon Bleu - 200 pesos")
    print("5. Menudo - 130 pesos")
    print("6. Macaroni Salad - 125 pesos")
    print("7. Carbonara - 135 pesos")
    print("8. Christmas Handaan Package - 1000 pesos")

# User's Order Processing Code
def take_order():
    total_price = 0
    ordered_items = []

    while True:
# Menu Display Code
        display_menu()

# User Input Code
        try:
            choice = int(input("Enter the number of the dish you'd like to order (or 0 to finish): "))
            if choice == 0:
                break  # Loop break code
            elif choice == 1:
                item, price = leche_flan()
            elif choice == 2:
                item, price = fruit_salad()
            elif choice == 3:
                item, price = mango_graham()
            elif choice == 4:
                item, price = cordon_bleu()
            elif choice == 5:
                item, price = menudo()
            elif choice == 6:
                item, price = macaroni_salad()
            elif choice == 7:
                item, price = carbonara()
            elif choice == 8:
                item, price = christmas_package()
            else:
                print("Invalid choice. Please select a valid menu number.")
                continue

# Item add code
            ordered_items.append(item)
            total_price += price
            print(f"Added {item} to your order for {price} pesos.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return ordered_items, total_price

# Bill Display Code
def display_bill(ordered_items, total_price):
    print("\nYour Order:")
    for item in ordered_items:
        print(f"- {item}")
    print(f"Total Price: {total_price} pesos")
    print("Thank you for ordering!")
    
# Billing code part
# Payment code
def process_payment(total_price):
    while True:
        try:
            bill = int(input("Enter the amount you wish to pay: "))
            if bill >= total_price:
                change = bill - total_price
                print(f"Payment successful! Your change is {change} pesos.")
                break
            else:
                print("Insufficient amount. Please enter an amount greater than or equal to the total price.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

# Main Function
def main():
    print("Welcome to the Food Ordering System!")
    ordered_items, total_price = take_order()
    display_bill(ordered_items, total_price)
    process_payment(total_price) 


if __name__ == "__main__":
    main()
