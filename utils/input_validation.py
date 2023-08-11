def get_integer_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"\nVeuillez enter un numéro entre {min_value} and {max_value}.\n")
        except ValueError:
            #TODO: Changer le message selon le menu du main_menu.
            print("\nERREUR /!\ ")
            print("Veuillez entrer un numéro valide.\n")