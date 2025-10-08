def add_menu_item(menu, item_name):
    """Adds a new item to the menu list."""
    if item_name not in menu:
        menu.append(item_name)
        print(f"-> Added '{item_name}' to the menu.")
    else:
        print(f"-> '{item_name}' is already on the menu.")

def remove_menu_item(menu, item_name):
    """Removes an item from the menu list. Handles cases where the item is not found."""
    try:
        menu.remove(item_name)
        print(f"-> Removed '{item_name}' from the menu.")
    except ValueError:
        print(f"-> Error: Cannot remove '{item_name}' because it is not currently on the menu.")

def check_availability(menu, item_name):
    """Checks if a specified item is currently on the menu."""
    if item_name in menu:
        return f"{item_name} is available"
    else:
        return f"{item_name} is currently unavailable"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
print("--- Starting Menu Operations ---")
add_menu_item(initial_menu, add_item)
remove_menu_item(initial_menu, remove_item)
print(f"\nUpdated menu: {initial_menu}")
availability_status = check_availability(initial_menu, check_item)
print(f"Availability: {availability_status}")