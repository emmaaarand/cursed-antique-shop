print("Welcome to The Cursed Antique Shop!")

cursed_antiques = [
    "Talisman", 
    "Monkeys Paw", 
    "Cursed Mirror", 
    "Haunted Painting", 
    "Voodoo Doll", 
    "Crystal Ball", 
    "Cursed Locket", 
    "Ancient Amulet", 
    "Phantom Clock", 
    "Dorian Gray's Portrait", 
    "Cursed Ring"
]

shopping_cart = [
    "Phantom Clock",
]

user_quit = False



while user_quit == False: 
    user_input  = input("""\nWhat would you like to do?
    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: """).lower()

    if user_input == "quit":
        user_quit = True
        break


    elif user_input == "buy":
        buy_option  = input("Would you like to buy the antique by name or by index? (Enter 'name' or 'index') ").lower()

        
        if buy_option == "name":
            item_choice = input("Which item would you like to buy? ")

            if item_choice in cursed_antiques:
                shopping_cart.append(item_choice)
                cursed_antiques.remove(item_choice)
                print(f"{item_choice} was removed from the inventory and added to the shopping cart.")
            else:
                print("That item is not available.")

        elif buy_option == "index":
            item_choice = input("Which item would you like to buy? ")

            if item_choice.isdigit():
                index_choice = int(item_choice) - 1
            
                if 0 <= index_choice < len(cursed_antiques):
                    selected_item = cursed_antiques.pop(index_choice)
                    shopping_cart.append(selected_item)
                    print(f"{selected_item} was removed from the inventory and added to the shopping cart.")
                else:
                    print("That item is not available.")

            else:
                print("That item is not available.")

        else:
            print("Sorry I didn't understand that.")


    elif user_input == "remove":
        remove_option = input("Which item would you like to remove from your shopping cart? ")

        try:
            shopping_cart.remove(remove_option)
            cursed_antiques.append(remove_option)
            print(f"{remove_option} was removed from the shopping cart.")

        except ValueError:
            print(f"{remove_option} is not in the shopping cart.")

    
    elif user_input == "sort":
        sort_option = input("Would you like to sort the antiques in reverse alphabetical order (y/n)? ").lower()

        

        if sort_option == "y":
            cursed_antiques.sort(reverse=True)
            print("Antiques sorted in reverse alphabetical order.")

        elif sort_option == "n":
            cursed_antiques.sort(reverse=False)
            print("Antiques sorted in alphabetical order.")

        else:
            print("Sorry I didn't understand that.")
     
    
    elif user_input == "list":
        list_choice = input("Would you like to view your shopping cart or available antiques (s/a)? ").lower()

        if list_choice == "s":
            for index, item in enumerate(shopping_cart):
                print(f"{index + 1}. {item}")

        elif list_choice == "a":
            for index, item in enumerate(cursed_antiques):
                print(f"{index + 1}. {item}")
        
        else:
            print("Sorry I didn't understand that.")
    
    
    else:
        print("Sorry I didn't understand that try again.")


print("\nThank you for visiting the Cursed Antiques Shop!")
