# Grocery Shopping List with Total Cost Calculator
# This program allows the user to input grocery items with prices and quantities,
# calculates the total cost, and saves the shopping list to a file.

# Create an empty list to store grocery items
grocery_items = []

# Variable to store the running total
total_cost = 0.0

print("Welcome to the Grocery Shopping List Program!")
print("Enter your grocery items.")
print("Type 'done' when finished or 'init file' to clear the saved file.\n")

while True:
    # Ask for item name
    user_input = input("Enter the item name: ")

    # Command to end program
    if user_input.lower() == "done":
        break

    # Command to clear the file
    if user_input.lower() == "init file":
        with open("grocery_output.txt", "w") as file:
            file.write("")  # Clear the file
        print("The grocery_output.txt file has been cleared.\n")
        continue  # Go back to asking for an item name

    # Ask for price per unit
    price = float(input(f"Enter the price for '{user_input}': $"))

    # Ask for quantity
    quantity = int(input(f"Enter the quantity for '{user_input}': "))

    # Calculate cost for this item
    item_total = price * quantity

    # Add to grocery list
    grocery_items.append((user_input, price, quantity, item_total))

    # Add to overall total
    total_cost += item_total

# Write results to file with calculation
with open("grocery_output.txt", "a") as file:
    file.write("Grocery Shopping List\n")
    file.write("====================\n")
    for item in grocery_items:
        file.write(f"{item[0]} - ${item[1]:.2f} x {item[2]} = ${item[3]:.2f}\n")
    file.write("\n")
    file.write(f"Total Cost: ${total_cost:.2f}\n")

# Display results to user
print("\nYour grocery list has been saved to 'grocery_output.txt'")
print(f"Total Cost: ${total_cost:.2f}")
