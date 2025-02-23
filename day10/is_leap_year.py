def is_leap_year(year):
    """
    This function checks if a year is a leap year or not.

    Args:
        year (int): Year to check.

    Returns:
        bool: True if leap year, False otherwise.
    """
    if year % 4 != 0:
        print(f"{year} is not divisible by 4")
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is divisible by 400")
            return True
        else:
            print(f"{year} is divisible by 100 but not by 400")
            return False
    else:
        print(f"{year} is divisible by 4 but not by 100")
        return True
            
# Call function
print(is_leap_year(2000)) # True