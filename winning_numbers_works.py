def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's guessed numbers match the predefined winning numbers.
    
    Parameters:
    user_list (list): A list of three integers representing the user's guessed numbers.
    winning_list (list): A list of three integers representing the winning numbers.
    
    Returns:
    str: A single word indicating the prize:
        - "First" if all three numbers match.
        - "Second" if two numbers match.
        - "Third" if one number matches.
        - "No" if none of the numbers match.
    """
    
   
    correct_guesses = len(set(user_list) & set(winning_list))
    
 
    if correct_guesses == 3:
        return "First"
    elif correct_guesses == 2:
        return "Second"
    elif correct_guesses == 1:
        return "Third"
    else:
        return "No"

#
winning_list = [5, 14, 17]
user_list = [19, 14, 17]
result = winning_numbers(user_list, winning_list)
print(result)  
user_list = [19, 14, 17]
result = winning_numbers(user_list, winning_list)
print(result)  