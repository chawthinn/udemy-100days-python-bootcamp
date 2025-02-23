def format_name(f_name, l_name):
    """
    This function takes in a first name and last name and returns the formatted name.

    Args:
        f_name (str): First name.
        l_name (str): Last name.

    Returns:
        str: Formatted name.
    """
    if f_name == "" or l_name == "":
        return
    formatted_f_name = f_name.title() 
    formatted_l_name = l_name.title()

    formatted_name = f"{formatted_f_name} {formatted_l_name}"

    return formatted_name

# Call function
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print(format_name(first_name, last_name))