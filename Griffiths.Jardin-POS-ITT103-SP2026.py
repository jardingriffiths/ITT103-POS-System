# this is the product catalog which has all the items the store sells
# each item has a price and how many are left in stock
inventory = {
    "Rice":        {"cost": 500,  "units": 20},
    "Flour":       {"cost": 350,  "units": 15},
    "Sugar":       {"cost": 280,  "units": 18},
    "Cooking Oil": {"cost": 750,  "units": 10},
    "Chubby Soda": {"cost": 220,  "units": 25},
    "Bread":       {"cost": 180,  "units": 30},
    "Butter":      {"cost": 400,  "units": 12},
    "Eggs":        {"cost": 150,  "units": 50},
    "Spice Bun":   {"cost": 600,  "units": 8},
    "Water":       {"cost": 100,  "units": 40}
}

# this basket holds whatever the cashier scans in
basket = {}

# this shows the main menu options to the cashier
def show_menu():
    print(" ")
    print("=============================")
    print("   Best Buy POS System")
    print("=============================")
    print("1. View Items")
    print("2. Scan item")
    print("3. Void item")
    print("4. View Basket")
    print("5. Process Payment")
    print("6. Exit")
    print("=============================")
    print(" ")

# this prints all items in the store with prices and stock levels
def show_inventory():
    print(" ")
    print("--- Store Inventory ---")
    print("Item              Cost     Units")
    print("-" * 35)
    for item, details in inventory.items():
        if details["units"] < 5:
            alert = " (running low)"
        else:
            alert = ""
        print(f"{item:<15} ${details['cost']:.2f}   {details['units']}{alert}")
    print(" ")

# this scans an item and adds it to the basket
def scan_item():
    show_inventory()
    entry = input("Enter item name: ").strip()

    if entry.title() not in inventory:
        print("That item is not in our inventory.")
        return

    entry = entry.title()

    if inventory[entry]["units"] == 0:
        print("Sorry, that item is currently unavailable.")
        return

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input, numbers only please.")
        return

    if qty <= 0:
        print("Quantity must be at least 1.")
        return

    if qty > inventory[entry]["units"]:
        print("Not enough stock, only", inventory[entry]["units"], "available.")
        return

    if entry in basket:
        basket[entry] = basket[entry] + qty
    else:
        basket[entry] = qty

    inventory[entry]["units"] = inventory[entry]["units"] - qty
    print("Scanned:", qty, "x", entry)
    print(" ")

# this removes an item from the basket and returns stock
def void_item():
    if len(basket) == 0:
        print("Basket is empty.")
        return

    entry = input("Which item to void? ").strip().title()
    if entry not in basket:
        print("That item is not in the basket.")
        return

    inventory[entry]["units"] = inventory[entry]["units"] + basket[entry]
    del basket[entry]
    print(entry, "has been voided.")
    print(" ")

# this shows everything that's currently in the basket
def show_basket():
    print(" ")
    print("--- Current Basket ---")
    if len(basket) == 0:
        print("Basket is empty.")
        return
    print("-" * 40)
    for item in basket:
        qty = basket[item]
        cost = inventory[item]["cost"]
        line_total = cost * qty
        print(item, "x", qty, "=", "$", line_total)
    print("-" * 40)
    print(" ")

# this prints the final receipt after payment
def print_receipt(subtotal, tax, discount, total, tendered, change):
    print(" ")
    print("================================")
    print("     BEST BUY RETAIL STORE      ")
    print("================================")
    print("          -- RECEIPT --         ")
    print("--------------------------------")
    for item in basket:
        qty = basket[item]
        cost = inventory[item]["cost"]
        line_total = cost * qty
        print(item, "x", qty, "=", "$", line_total)
    print("--------------------------------")
    print("Subtotal:   $", subtotal)
    print("Tax (10%):  $", tax)
    if discount > 0:
        print("Discount:   $", discount)
    print("Total:      $", total)
    print("Tendered:   $", tendered)
    print("Change:     $", change)
    print("--------------------------------")
    print("      Thank you, come again!    ")
    print("================================")
    print(" ")

# this calculates the total while applying tax and discount then takes the payment
def process_payment():
    if not basket:
        print("Nothing scanned yet.")
        return

    subtotal = 0
    for item in basket:
        subtotal = subtotal + (inventory[item]["cost"] * basket[item])

    tax = subtotal * 0.10

    if subtotal > 5000:
        discount = subtotal * 0.05
        print("5% loyalty discount applied!")
    else:
        discount = 0

    total = subtotal + tax - discount

    print(" ")
    print("Subtotal:   $", subtotal)
    print("Tax:        $", tax)
    if discount > 0:
        print("Discount:   $", discount)
    print("Amount Due: $", total)

    while True:
        try:
            tendered = float(input("Amount tendered: $"))
            if tendered < total:
                print("Insufficient, amount due is $", total)
            else:
                break
        except ValueError:
            print("Numbers only please.")

    change = tendered - total
    print("Change: $", change)
    print(" ")

    print_receipt(subtotal, tax, discount, total, tendered, change)
    basket.clear()
    print("Payment complete. Next customer please.")
    print(" ")

# this is the main loop that keeps the register running
def run_register():
    print("Best Buy POS System - Ready")
    while True:
        show_menu()
        selection = input("Select option (1-6): ").strip()

        if selection == "1":
            show_inventory()
        elif selection == "2":
            scan_item()
        elif selection == "3":
            void_item()
        elif selection == "4":
            show_basket()
        elif selection == "5":
            process_payment()
        elif selection == "6":
            print("Closing register. Goodbye!")
            break
        else:
            print("Invalid selection, enter a number between 1 and 6.")

run_register()

#I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE FOR THIS ASSIGNMENT